from typing import Any, Dict, Optional
import httpx
import json
import logging
from fastapi import HTTPException
from app.core.logging_config import configure_logging
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
        # self.cache_key = None

    async def _request(
        self,
        method: str,
        endpoint: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        if endpoint.startswith("http"):
            url = endpoint
        else:
            url = f"{self.base_url}{endpoint}"

        headers = headers or {}
        params = params or {}

        if self.api_key:
            if self.api_key_location == "header":
                headers[self.api_key_name] = self.api_key
            elif self.api_key_location == "query":
                params[self.api_key_name] = self.api_key

        attempt = 0
        while attempt < self.retry_attempts:
            try:
                logger.debug("Attempting to hit API endpoint...")
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
                raise HTTPException(
                    status_code=500, detail=f"Invalid JSON response from API: {e}"
                )

            except httpx.RequestError as e:
                logger.error(f"Request error (attempt {attempt + 1}): {e}")
                if (
                    isinstance(e, httpx.TimeoutException)
                    and attempt < self.retry_attempts - 1
                ):
                    attempt += 1
                    await asyncio.sleep(self.retry_delay)
                    continue  # Retry

                # If not a timeout or max attempts reached, raise an HTTPException
                raise HTTPException(
                    status_code=500,
                    detail=f"Request error after {attempt + 1} attempts: {e}",
                )

            except Exception as e:
                logger.error(f"Unexpected exception: {e}")
                raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

            attempt += 1

        raise HTTPException(status_code=500, detail="Max retry attempts reached")

    async def get(
        self,
        endpoint: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        return await self._request("GET", endpoint, params, headers)

    async def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        return await self._request("POST", endpoint, data, headers)

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()
