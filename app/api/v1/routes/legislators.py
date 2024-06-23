from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, Request
from app.schemas.opensecrets import Legislator
from app.core.utilities import clean_legislator_data, validate_state_id
from app.core.dependencies import get_opensecrets_client, get_fec_client, get_cdg_client
from app.core.redis import get_redis_client
from app.services import (
    OpenSecretsAsyncAPIClient,
    FECAsyncAPIClient,
    CongressAPIAsyncClient,
)
from typing import Any, Dict, List, Optional, Union
import logging
import redis.asyncio as redis
import httpx
from fastapi_limiter.depends import RateLimiter


router = APIRouter()
logger = logging.getLogger(__name__)

async def fetch_legislator_data(
    client: Optional[
        Union[OpenSecretsAsyncAPIClient, FECAsyncAPIClient, CongressAPIAsyncClient]
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


@router.get("/legislator/{cid}", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_legislator_info(
    request:Request,
    cid: str,
    background_tasks: BackgroundTasks,
    client: OpenSecretsAsyncAPIClient = Depends(get_opensecrets_client),
    redis_client: redis.Redis = Depends(get_redis_client),
) -> Legislator:
    legislator_data = await fetch_legislator_data(
        client=client, method="get_legislator", redis_client=redis_client, cid=cid
    )
    legislator_attributes = (
        legislator_data.get("response", {})
        .get("legislator", {})
        .get("@attributes", None)
    )
    logger.debug(legislator_attributes)
    if legislator_attributes:
        legislator_attributes = clean_legislator_data(legislator_attributes)
        return Legislator(**legislator_attributes)
    else:
        raise HTTPException(status_code=404, detail="Legislator not found")


@router.get("/state/{state_id}", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_state_legislator_info(
    background_tasks: BackgroundTasks,
    state_id: str = Depends(validate_state_id),
    client: OpenSecretsAsyncAPIClient = Depends(get_opensecrets_client),
    redis_client: redis.Redis = Depends(get_redis_client),
) -> List[Legislator]:
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_legislators_by_state",
        redis_client=redis_client,
        state_id=state_id,
    )
    legislators = [
        clean_legislator_data(legislator.get("@attributes", {}))
        for legislator in legislator_data.get("response", {}).get("legislator", [])
    ]
    return [Legislator(**legislator) for legislator in legislators if legislator]


@router.get("/candidate/{candidate_id}", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_fec_candidate_info(
    background_tasks: BackgroundTasks,
    candidate_id: str,
    client: FECAsyncAPIClient = Depends(get_fec_client),
    redis_client: redis.Redis = Depends(get_redis_client),
):
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_candidate",
        redis_client=redis_client,
        candidate_id=candidate_id,
    )
    logger.debug(legislator_data)


@router.get("/congress/{bioguideId}", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_cdg_data(
    background_tasks: BackgroundTasks,
    bioguideId: str,
    client: CongressAPIAsyncClient = Depends(get_cdg_client),
    redis_client: redis.Redis = Depends(get_redis_client),
):
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_member_info",
        redis_client=redis_client,
        bioguideId=bioguideId,
    )
    return legislator_data

@router.get("/congress/{bioguideId}/sponsored_legislation", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_sponsored_legislation(
    background_tasks: BackgroundTasks,
    bioguideId: str,
    offset: int,
    limit: int = 250,
    client: CongressAPIAsyncClient = Depends(get_cdg_client),
    redis_client: redis.Redis = Depends(get_redis_client),
):
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_sponsored_legislation",
        redis_client=redis_client,
        bioguideId=bioguideId,
        limit=limit,
        offset=offset,
    )
    return legislator_data

@router.get("/congress/{bioguideId}/all_sponsored_legislation", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def get_all_sponsored_legislation(
    background_tasks: BackgroundTasks,
    bioguideId: str,
    offset: int,
    limit: int = 250,
    client: CongressAPIAsyncClient = Depends(get_cdg_client),
    redis_client: redis.Redis = Depends(get_redis_client),
):
    legislator_data = await fetch_legislator_data(
        client=client,
        method="get_all_sponsored_legislation",
        redis_client=redis_client,
        bioguideId=bioguideId,
        limit=limit,
        offset=offset,
    )
    return legislator_data
