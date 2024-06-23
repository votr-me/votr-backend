"""Asynchronous Client for the Congress.gov API.

This client provides methods to interact with the Congress.gov API,
offering efficient retrieval of member information and sponsored legislation
data. It leverages caching (via Redis) to optimize performance and reduce API
usage.

Features:

* Asynchronous operations for concurrent API requests.
* Caching of API responses for faster retrieval.
* Automatic pagination handling for large datasets.
* Robust error handling for API and network issues.
"""


from typing import Any, Dict
from app.core.config import config
from .BaseAsyncAPIClient import BaseAsyncAPIClient
import redis.asyncio as redis

import logging
from app.core.logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)
class CongressAPIAsyncClient(BaseAsyncAPIClient):
    
    """
    Initializes the client.

    Args:
        api_key (str): Your Congress.gov API key.
        service_name (str, optional): A name to identify the API in logs (default: "congress_dot_gov").
        api_key_name (str, optional): The name of the API key parameter (default: "X-API-Key").
        api_key_location (str, optional): The location of the API key ("header" or "query", default: "header").
    """
    def __init__(
        self,
        api_key: str,
        service_name: str,
        api_key_name: str = "apikey",
        api_key_location="header",
    ) -> None:
        base_url = config.BASE_URL_CONGRESS_API
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            api_key_name=api_key_name,
            service_name=service_name,
            api_key_location=api_key_location,
        )

    async def get_member_info(
        self, bioguideId: str, redis_client: redis.Redis = None
    ) -> Dict[str, Any]:
        """
        Fetches information about a member of Congress.

        Args:
            bioguideId (str): The member's Bioguide ID.
            redis_client (redis.Redis, optional): A Redis client for caching (if enabled).

        Returns:
            Dict[str, Any]: The member's information.
        """
        endpoint = f"member/{bioguideId}"
        params = {"format": "json"}
        return await self.get(endpoint, params, redis_client)

    async def get_sponsored_legislation(
        self, bioguideId: str, limit: int, offset: int, redis_client: redis.Redis = None
    ) -> Dict[str, Any]:
        """
        Fetches a paginated list of legislation sponsored by a member of Congress.

        Args:
            bioguideId (str): The member's Bioguide ID.
            limit (int): Maximum number of results per page.
            offset (int): Number of results to skip (for pagination).
            redis_client (redis.Redis, optional): A Redis client for caching (if enabled).

        Returns:
            Dict[str, Any]: The paginated response containing sponsored legislation data.
        """
        endpoint = f"member/{bioguideId}/sponsored-legislation"
        params = {"format": "json", "offset": offset, "limit": limit}        
        response = await self.get(endpoint, params, redis_client) 
        return response 
    
    async def get_all_sponsored_legislation(
        self, bioguideId: str, limit: int, offset: int, redis_client: redis.Redis = None
    ) -> Dict[str, Any]:
        """
        Fetches all legislation sponsored by a member of Congress, handling pagination automatically.

        Args:
            bioguideId (str): The member's Bioguide ID.
            limit (int, optional): Maximum number of results per page (default: 250).
            offset (int, optional): Initial offset for pagination (default: 0).
            redis_client (redis.Redis, optional): A Redis client for caching (if enabled).

        Returns:
            List[Dict[str, Any]]: A list of all sponsored legislation data.
        """
        
        endpoint = f"member/{bioguideId}/sponsored-legislation"
        params = {"format": "json", "offset": offset, "limit": limit}        
        response = await self.get(endpoint, params, redis_client) 
        all_legislation = response.get('sponsoredLegislation', None)
        total_count = response.get('pagination', {}).get('count', None)
        logger.debug(f'Retrieving first {offset}, will retrieve {response.get("pagination", {}).get("count", None)}')

        while len(all_legislation) < total_count:
            logger.debug(f"Retrieving bills from: {response.get('pagination', {}).get('next', None)}")
            response = await self.get_full_url(
                url = response.get('pagination', {}).get('next', None),
                redis_client=redis_client,
            )
            
            if response.get('sponsoredLegislation', None):
                all_legislation.extend(response.get('sponsoredLegislation', None)) 
    
        logger.debug(f'Retrieved {len(all_legislation)} pieces of legislation')
        
        return all_legislation 

congress_async_api_client = CongressAPIAsyncClient(
        api_key=config.CONGRESS_GOV_API_KEY,
        service_name="congress_dot_gov",
        api_key_name="X-Api-Key",
    )