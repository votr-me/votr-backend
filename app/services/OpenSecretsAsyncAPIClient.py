from .BaseAsyncAPIClient import BaseAsyncAPIClient
from typing import Dict, Any
from app.core.config import config


class OpenSecretsAsyncAPIClient(BaseAsyncAPIClient):
    def __init__(
        self,
        api_key: str,
        service_name: str,
        api_key_name: str = "apikey",
        api_key_location="query",
    ) -> None:
        base_url = config.BASE_URL_OPENSECRETS_API
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            api_key_name=api_key_name,
            service_name=service_name,
            api_key_location=api_key_location,
        )

    async def get_legislators_by_state(self, state_id: str) -> Dict[str, Any]:
        endpoint = ""
        params = {"method": "getLegislators", "id": state_id, "output": "json"}
        return await self.get(endpoint, params)

    async def get_legislator(self, cid: str) -> Dict[str, Any]:
        endpoint = ""
        params = {"method": "getLegislators", "id": cid, "output": "json"}
        return await self.get(endpoint, params)


open_secrets_async_client = OpenSecretsAsyncAPIClient(
    api_key=config.OPENSECRETS_API_KEY, service_name="opensecrets"
)
