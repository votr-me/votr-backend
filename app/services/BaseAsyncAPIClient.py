from typing import Any, Dict, Optional
import httpx
import json
import logging
import redis.asyncio as redis
from fastapi import HTTPException
from app.core.logging_config import configure_logging
import hashlib
import urllib.parse
import asyncio

configure_logging()
logger = logging.getLogger(__name__)

class BaseAsyncAPIClient:
    def __init__(
        self,
        service_name: str,
        base_url: str,
        api_key: Optional[str] = None,
        api_key_name: str = "apikey",
        api_key_location: str = "header",
        retry_attempts: int = 3,
        retry_delay: int = 2,  # Delay in seconds
    ) -> None:
        self.service_name = service_name
        self.base_url = base_url
        self.api_key = api_key
        self.api_key_name = api_key_name
        self.api_key_location = api_key_location
        self.client = httpx.AsyncClient()
        self.retry_attempts = retry_attempts
        self.retry_delay = retry_delay

    def create_cache_key(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        method: str = "GET",
    ) -> str:
        params = params or {}
        sorted_params = sorted({key: value for key, value in params.items() if key not in ['api_key', 'api_key_name']}.items())
        encoded_params = urllib.parse.urlencode(sorted_params)
        raw_key = f"{method}|{endpoint}|{self.service_name}|{encoded_params}"
        hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()
        
        return hashed_key
    
    def create_cache_key_full_url(
        self,
        url: str,
        method: str = "GET",
    ) -> str:
        raw_key = f"{method}|{url}|{self.service_name}"
        hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()
        
        return hashed_key

    async def get_full_url(
        self,
        url: str,
        redis_client: Optional[redis.Redis] = None,
        headers: Optional[Dict[str, str]] = None,
        cache_ttl: int = 3600,
    ) -> Dict[str, Any]:
        return await self._request("GET", url, None, headers, redis_client, cache_ttl)
    
    async def _request(
        self,
        method: str,
        endpoint: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        redis_client: Optional[redis.Redis] = None,
        cache_ttl: int = 3600,
    ) -> Dict[str, Any]:
        
        # Check if the endpoint is a full URL
        if endpoint.startswith("http"):
            url = endpoint
            cache_key = self.create_cache_key_full_url(url, method)
        else:
            url = f"{self.base_url}{endpoint}"
            cache_key = self.create_cache_key(endpoint, params, method)
            
        headers = headers or {}
        params = params or {}

        if self.api_key:
            if self.api_key_location == "header":
                headers[self.api_key_name] = self.api_key
            elif self.api_key_location == "query":
                params[self.api_key_name] = self.api_key

        if redis_client:
            try:
                cached_data = await redis_client.get(cache_key)
                if cached_data:
                    logger.debug(f"Cache hit for: {cache_key}")
                    return json.loads(cached_data)
            except redis.RedisError as e:
                logger.error(f"Redis error during get: {e}")
                raise HTTPException(
                    status_code=503, detail="Caching service unavailable"
                )
        else:
            logger.warning(f"No Cache hit for: {cache_key}")
        
        attempt = 0

        while attempt <= self.retry_attempts:
            try:
                response = await self.client.request(
                    method, url, params=params, headers=headers
                )
                response.raise_for_status()

                if 200 <= response.status_code < 300:
                    data = response.json()
                    return data

                if not response.content:
                    raise HTTPException(
                        status_code=500, detail="No data returned from API"
                    )
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP error: {e}")
                raise HTTPException(status_code=e.response.status_code, detail=str(e))

            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error: {e}")
                raise HTTPException(status_code=500, detail=f"Invalid JSON response from API: {e}")

            except httpx.RequestError as e:
                try:
                    if isinstance(e, httpx.TimeoutException) and attempt < self.retry_attempts:
                        attempt += 1
                        await asyncio.sleep(self.retry_delay)
                        continue  # Retry

                    logger.error(f"Request error (attempt {attempt}): {e}")  
                    raise HTTPException(status_code=500, detail=f"Request error: {e}")

                except Exception as inner_e:
                    logger.error(f"Unexpected exception during retry: {inner_e}")
                    raise  # Re-raise the inner_e to propagate the error
                
    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        redis_client: Optional[redis.Redis] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        return await self._request("GET", endpoint, params, headers, redis_client)

    async def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        redis_client: Optional[redis.Redis] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        return await self._request("POST", endpoint, data, headers, redis_client)

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()
