import logging
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Query, Request, Response
from app.core.dependencies import get_geocodio_client
from app.services import GeocodioAsyncAPIClient
from app.db.crud.crud_congress_member import CongressMemberCRUD
from app.schemas.congress.congress_members import CongressMemberSchema
from app.db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import json
from app.core.logging_config import configure_logging
from app.core.redis import RedisPool, get_redis_pool
from fastapi_cache.decorator import cache
import hashlib

router = APIRouter()


configure_logging()
logger = logging.getLogger("app")

@router.get(
    "/my_legislators",
    status_code=200,
)
@cache(expire=60)
async def get_user_location_info(
    request: Request,
    response: Response,
    redis: RedisPool = Depends(get_redis_pool),
    session: AsyncSession = Depends(get_session),
    client: GeocodioAsyncAPIClient = Depends(get_geocodio_client),
    address: str = Query(..., description="The address to geolocate"),
    fields: List[str] = Query(
        default=["cd"],
        description="List of fields to return from geocodio API (e.g. stateleg, cd)",
    ),
) -> List[CongressMemberSchema]:
    try:

        response.set_cookie(key="user_address", value="8 Delaware Road Medfield MA 02052", httponly=True, secure=True)
        geolocation_data = await client.geolocate(
            address=address,
            fields=fields,
        )

        if not geolocation_data:
            raise HTTPException(status_code=404, detail="No results found")

        if geolocation_data:
            _legislators = []
            for id in geolocation_data.get("bioguide_ids", []):
                cached_legislator = await redis.get(f"legislator:{id}")
                if cached_legislator:
                    logger.debug(f'Cache hit for legislator {id}')
                    legislator_schema = CongressMemberSchema(**json.loads(cached_legislator))
                else:
                    _legislator = await CongressMemberCRUD(db=session).get_by_bioguide_id(
                        bioguide_id=id
                    )
                    if _legislator:
                        legislator_schema = CongressMemberSchema.from_orm(_legislator)
                        await redis.set(f"legislator:{id}", json.dumps(legislator_schema.model_dump()))
                _legislators.append(legislator_schema)

            if len(_legislators) == 0:
                raise HTTPException(
                    status_code=500,
                    detail=f'No Legislators found for {geolocation_data.get("address", None)}',
                )

            if _legislators:
                
                # Serialize Pydantic models to JSON
                serialized_legislators = json.dumps(
                    [legislator.dict() for legislator in _legislators]
                )

                # Store the serialized legislators data in a cookie
                response.set_cookie(
                    key="legislators",
                    value=serialized_legislators,
                    httponly=True,
                    secure=True,
                )
            return _legislators

    except HTTPException as e:
        logger.error(f"Geolocation error for address '{address}': {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error for address '{address}': {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
