import logging
from httpx import AsyncClient
from abc import ABC, abstractmethod
from app.core.config import config

logger = logging.getLogger(__name__)


class GeocodioRepositoryInterface(ABC):
    @abstractmethod
    async def get_address_info(self, address: str) -> dict:
        pass


class GeocodioRepository(GeocodioRepositoryInterface):
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def get_address_info(self, address: str) -> dict:
        url = config.GEOCODIO_BASE_URL
        params = {"q": address, "fields": ["cd"], "api_key": self.api_key}

        async with AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
