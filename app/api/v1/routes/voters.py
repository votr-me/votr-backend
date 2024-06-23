from fastapi import APIRouter, HTTPException, Depends, Query, BackgroundTasks
from typing import List, Optional, Union, Any, Dict
import logging
from app.core.utilities import parse_geocodio_fields
from app.core.dependencies import get_geocodio_client
from app.core.logging_config import configure_logging
from app.services import GeocodioAsyncAPIClient
import redis.asyncio as redis
from app.core.redis import get_redis_client
from fastapi_limiter.depends import RateLimiter
import httpx


router = APIRouter()

configure_logging()
logger = logging.getLogger(__name__)


async def fetch_geocodio_data(
    client: Optional[
        Union[GeocodioAsyncAPIClient]
    ],
    method: str,
    redis_client: redis.Redis,
    **kwargs: Any,
) -> Dict[str, Any]:
    try:
        response = await getattr(client, method)(redis_client=redis_client, **kwargs)
        return response
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except AttributeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid method: {method} - {e}")


@router.get("/geolocate", status_code=200, dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_user_location_info(
    background_tasks: BackgroundTasks,
    client: GeocodioAsyncAPIClient = Depends(get_geocodio_client),
    address: str = Query(..., description="The address to geolocate"),
    fields: List[str] = Depends(parse_geocodio_fields),
    redis_client: redis.Redis = Depends(get_redis_client),
):
    try:
        geolocation_data = await fetch_geocodio_data(
            client=client,
            method='geolocate',
            redis_client=redis_client,
            address=address,
            fields=fields
        )
        return geolocation_data
    except HTTPException as e:
        logger.error(f"Geolocation error for address '{address}': {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error for address '{address}': {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
