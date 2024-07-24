import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logging_config import configure_logging
from app.core.redis import get_redis_pool, RedisPool
from app.db.crud_congress_member import congress_member
from app.db.session import get_db
from app.schemas.congress.congress_members import CongressMemberOut

configure_logging()
logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/", response_model=List[CongressMemberOut])
async def read_congress_members(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await congress_member.get_multi(db, skip=skip, limit=limit)


@router.get("/{bioguide_id}", response_model=CongressMemberOut)
async def read_congress_member(
        bioguide_id: str,
        db: AsyncSession = Depends(get_db),
        redis: RedisPool = Depends(get_redis_pool)
):
    # Check if the result is in the cache
    cached_result = await redis.get(bioguide_id)
    if cached_result:
        logger.debug(f"Cache hit for {bioguide_id}")
        return CongressMemberOut.parse_raw(cached_result)

    # If not in the cache, query the database
    db_congress_member = await congress_member.get_by_bioguide_id(db, bioguide_id=bioguide_id)
    if db_congress_member is None:
        raise HTTPException(status_code=404, detail="CongressMember not found")

    # Convert to Pydantic model
    result = CongressMemberOut.from_orm(db_congress_member)

    # Cache the result
    await redis.set(bioguide_id, result.json(), expire=3600)
    logger.debug(f"Cache set for {bioguide_id}")

    return result
