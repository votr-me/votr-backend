import logging
from typing import Dict, Any, List, Optional

import httpx
from fastapi import HTTPException
import us
from app.core.config import config
from app.schemas.voters.voters import VoterInfo
import json

from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")


class GeocodioAsyncAPIClient:
    def __init__(
        self,
        api_key: str,
    ) -> None:
        self.base_url = config.GEOCODIO_BASE_URL
        self.client = httpx.AsyncClient()
        self.api_key = api_key

    def extract_voter_information(self, geolocation_data: Dict) -> VoterInfo:
        voter_info = {
            "state": geolocation_data.get("input", {})
            .get("address_components", {})
            .get("state", None),
            "state_fips": str(
                us.states.lookup(
                    geolocation_data.get("input", {})
                    .get("address_components", {})
                    .get("state", None)
                ).fips
            ).rjust(2, "0"),
            "address": geolocation_data.get("input", {}).get("formatted_address", None),
            "district_name": geolocation_data.get("results")[0]
            .get("fields", {})
            .get("congressional_districts", {})[0]
            .get("name", None),
            "district_number": str(
                geolocation_data.get("results")[0]
                .get("fields", {})
                .get("congressional_districts", {})[0]
                .get("district_number")
            ).rjust(2, "0"),
            "bioguide_ids": [
                legislator.get("references", {}).get("bioguide_id", None)
                for legislator in geolocation_data.get("results")[0]
                .get("fields", {})
                .get("congressional_districts", {})[0]
                .get("current_legislators", {})
            ],
        }

        return voter_info

    async def _get(
        self,
        endpoint: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        headers = headers or {}
        params = params or {}

        if endpoint.startswith("http"):
            url = endpoint
        else:
            url = f"{self.base_url}{endpoint}"

        if self.api_key:
            try:
                params["api_key"] = self.api_key
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Unexpected Error: {e}")
        else:
            raise HTTPException(status_code=403, detail="Invalid API Key")

        try:
            response = await self.client.request(
                "GET", url, params=params, headers=headers
            )
            response.raise_for_status()

            if 200 <= response.status_code < 300:
                data = response.json()
                return data
            if not response.content:
                raise HTTPException(status_code=500, detail="No data returned from API")

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e}")
            status_code = e.response.status_code if e.response else 500
            detail = str(e) or "Unknown HTTP error"
            return {"error": detail}, status_code  # Return error details and status

        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            raise HTTPException(
                status_code=500, detail=f"Invalid JSON response from API: {e}"
            )
        except Exception as e:
            logger.error(f"Unexpected exception: {e}")
            raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

    async def geolocate(self, address: str, fields: List[str]) -> Dict[str, Any]:
        try:
            params = {"q": address, "fields": fields}
            result = await self._get(endpoint="geocode", params=params)
            return self.extract_voter_information(result)

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error for address '{address}': {e.response.json()}")
            raise HTTPException(
                status_code=e.response.status_code, detail=e.response.json()
            )
        except Exception as e:
            logger.exception(f"Unexpected error for address '{address}': {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self


geocodio_async_client = GeocodioAsyncAPIClient(
    api_key=config.GEOCODIO_API_KEY,
)
