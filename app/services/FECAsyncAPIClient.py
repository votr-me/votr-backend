from .BaseAsyncAPIClient import BaseAsyncAPIClient
from app.core.config import config
from typing import Dict, Any
import redis.asyncio as redis


class FECAsyncAPIClient(BaseAsyncAPIClient):
    def __init__(
        self,
        api_key: str,
        service_name: str,
        api_key_name: str = "X-Api-Key",
    ) -> None:
        base_url = config.FEC_BASE_URL
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            api_key_name=api_key_name,
            service_name=service_name,
        )

    async def get_candidate(
        self, candidate_id: str, redis_client: redis.Redis = None
    ) -> Dict[str, Any]:
        endpoint = f"candidates/{candidate_id}/"
        return await self.get(endpoint, redis_client=redis_client)

fec_async_client = FECAsyncAPIClient(api_key=config.FEC_API_KEY, service_name="fec")