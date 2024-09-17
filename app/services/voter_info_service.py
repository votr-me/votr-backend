from app.data import GeocodioRepositoryInterface


class AddressService:
    def __init__(self, geocodio_repo: GeocodioRepositoryInterface):
        self.geocodio_repo = geocodio_repo

    async def get_address_details(self, address: str) -> dict:
        data = await self.geocodio_repo.get_address_info(address)

        return data
