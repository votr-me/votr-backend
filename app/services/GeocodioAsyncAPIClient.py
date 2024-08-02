import logging
from typing import Dict, Any, List

import httpx
from fastapi import HTTPException

from app.core.config import config
from app.core.logging_config import configure_logging
from .BaseAsyncAPIClient import BaseAsyncAPIClient

configure_logging()
logger = logging.getLogger(__name__)


class GeocodioAsyncAPIClient(BaseAsyncAPIClient):
    def __init__(
        self,
        api_key: str,
        service_name: str,
        api_key_name: str,
        api_key_location: str = "query",
    ) -> None:
        base_url = config.GEOCODIO_BASE_URL
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            api_key_name=api_key_name,
            service_name=service_name,
            api_key_location=api_key_location,
        )

    async def geolocate(self, address: str, fields: List[str]) -> Dict[str, Any]:
        try:
            params = {
                "q": address,
                "fields": fields,  # ",".join(fields) if fields else None,
            }
            result = await self.get("geocode", params)
            return result
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error for address '{address}': {e.response.json()}")
            raise HTTPException(
                status_code=e.response.status_code, detail=e.response.json()
            )
        except Exception as e:
            logger.exception(f"Unexpected error for address '{address}': {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")


geocodio_async_client = GeocodioAsyncAPIClient(
    api_key=config.GEOCODIO_API_KEY,
    service_name="geocodio",
    api_key_name="api_key",
)
