from app.core.dependencies import get_geocodio_client
from app.core.logging_config import configure_logging
from app.services import GeocodioAsyncAPIClient
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi_cache.decorator import cache
from fastapi_limiter.depends import RateLimiter
from typing import List, Optional, Union, Any, Dict
import httpx
import logging

router = APIRouter()

configure_logging()
logger = logging.getLogger(__name__)


async def fetch_geocodio_data(
    client: Optional[Union[GeocodioAsyncAPIClient]],
    method: str,
    **kwargs: Any,
) -> Dict[str, Any]:
    try:
        response = await getattr(client, method)(**kwargs)
        return response
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except AttributeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid method: {method} - {e}")


@router.get(
    "/geolocate",
    status_code=200,
    dependencies=[Depends(RateLimiter(times=10, seconds=60))],
)
@cache(expire=3600)
async def get_user_location_info(
    client: GeocodioAsyncAPIClient = Depends(get_geocodio_client),
    address: str = Query(..., description="The address to geolocate"),
    fields: List[str] = Query(
        ..., description="List of fields to return (e.g. stateleg, cd)"
    ),
):
    try:
        geolocation_data = await fetch_geocodio_data(
            client=client,
            method="geolocate",
            address=address,
            fields=fields,
        )
        return geolocation_data
    except HTTPException as e:
        logger.error(f"Geolocation error for address '{address}': {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error for address '{address}': {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
