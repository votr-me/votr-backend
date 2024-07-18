from app.core.dependencies import get_cdg_client
from app.core.utilities import generate_param_hash, custom_cache_key_generator
from app.services import (
    OpenSecretsAsyncAPIClient,
    FECAsyncAPIClient,
    CongressAPIAsyncClient,
)
from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    Query,
    Request,
)
import json
from fastapi_cache.decorator import cache
from typing import Any, Dict, Optional, Union
import httpx
import logging
from app.core.utilities import generic_cache_key_builder
from app.core.logging_config import configure_logging
from app.core.analytics import SponsoredLegislation
from fastapi_cache import FastAPICache

router = APIRouter()

configure_logging()
logger = logging.getLogger(__name__)


async def fetch_legislator_data(
    client: Optional[
        Union[OpenSecretsAsyncAPIClient, FECAsyncAPIClient, CongressAPIAsyncClient]
    ],
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


async def fetch_legislation_analytics(
    client: CongressAPIAsyncClient, bioguideId: str, offset: int, limit: int
) -> SponsoredLegislation:
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_all_sponsored_legislation",
        bioguideId=bioguideId,
        limit=limit,
        offset=offset,
    )
    return SponsoredLegislation(sponsored_legislation_response=legislator_data)


async def get_legislation_analytics(
    bioguideId: str,
    offset: int = 0,
    limit: int = 250,
    client: CongressAPIAsyncClient = Depends(get_cdg_client),
) -> SponsoredLegislation:
    return await fetch_legislation_analytics(client, bioguideId, offset, limit)


@router.get("/congress/sponsored_legislation_all/")
@cache(expire=36000, key_builder=generic_cache_key_builder)
async def get_all_sponsored_legislation(
    request: Request,
    client: CongressAPIAsyncClient = Depends(get_cdg_client),
    bioguideId: str = Query(..., description="bioguideId for legislator"),
    offset: int = Query(0, description="index to start at"),
    limit: int = Query(250, description="Number of bills to return at once (max 250)"),
):
    logger.debug(f"Request: {request}")
    logger.debug(
        generic_cache_key_builder(
            func="get_all_sponsored_legislation",
            bioguideId=bioguideId,
            offset=offset,
            limit=limit,
            request=request,
        )
    )
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_all_sponsored_legislation",
        bioguideId=bioguideId,
        limit=limit,
        offset=offset,
    )
    return legislator_data


async def get_cached_all_sponsored_legislation(
    request: Request, bioguideId: str, offset: int, limit: int
):
    # Generate the param hash
    query_params = {"bioguideId": bioguideId, "offset": offset, "limit": limit}
    param_hash = generate_param_hash(query_params)

    # Construct the cache key
    cache_key = custom_cache_key_generator(
        prefix="votr",
        namespace="api:v1:legislators:congress:sponsored_legislation_all",
        identifier=bioguideId,
        param_hash=param_hash,
    )
    logger.debug(cache_key)

    cache_instance = FastAPICache.get_backend()
    cached_data = await cache_instance.get(cache_key)

    if not cached_data:
        raise HTTPException(status_code=404, detail="Data not found in cache")

    _sponsored_legislation = await SponsoredLegislation(
        sponsored_legislation_response=json.loads(cached_data)
    ).initialize()
    return _sponsored_legislation


@router.get("/congress/sponsored_legislation_summary/")
async def get_sponsored_legislation_summary(
    request: Request,
    congress: int = Query(..., description="Congress number for legislator"),
    legislation_type: str = Query(..., description="Type of legislation"),
    analytics: SponsoredLegislation = Depends(get_cached_all_sponsored_legislation),
):
    return await analytics.get_sponsored_legislation_by_congress(congress)
