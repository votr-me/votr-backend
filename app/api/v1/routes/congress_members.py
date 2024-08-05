import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

import json
from app.core.logging_config import configure_logging
from app.core.redis import get_redis_pool, RedisPool
from app.db.crud.crud_congress_member import CongressMemberCRUD
from app.db.session import get_db
from app.schemas.congress.congress_members import CongressMemberSchema
from app.db.models.congress_members import CongressMember

configure_logging()
logger = logging.getLogger(__name__)
router = APIRouter()

# @router.get("/", response_model=List[CongressMemberSchema])
# async def read_congress_members(
#     skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
# ):
#     """
#     Fetch multiple Congress members from the database.

#     Args:
#         skip (int): The number of records to skip.
#         limit (int): The number of records to return.
#         db (AsyncSession): The database session.

#     Returns:
#         List[CongressMember]: List of Congress members.
#     """
#     try:
#         members = await congress_member.get_multi(db, skip=skip, limit=limit)
#         return members
#     except Exception as e:
#         logger.error(f"Error fetching congress members: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get(
    "/{bioguide_id}",
)  # response_model=CongressMemberSchema)
async def read_congress_member(
    bioguide_id: str,
    db: AsyncSession = Depends(get_db),
    redis: RedisPool = Depends(get_redis_pool),
):
    """
    Fetch a single Congress member by bioguide ID. Uses Redis for caching to improve performance.

    Args:
        bioguide_id (str): The bioguide ID of the Congress member.
        db (AsyncSession): The database session.
        redis (RedisPool): The Redis connection pool.

    Returns:
        CongressMember: The Congress member data.
    """
    if not bioguide_id:
        logger.warning("Invalid bioguide_id provided.")
        raise HTTPException(status_code=400, detail="Invalid bioguide_id")
    else:
        logger.debug(f"Fetching data for {bioguide_id}")

    try:
        # Check if the result is in the cache
        cached_result = await redis.get(bioguide_id)

        if cached_result:
            logger.debug(f"Cache hit for {bioguide_id}")
            return JSONResponse(
                content=json.loads(cached_result), media_type="application/json"
            )

        crud = CongressMemberCRUD(CongressMember)
        db_congress_member = await crud.get_by_bioguide_id(db, bioguide_id=bioguide_id)
        db_congress_member_sponsorship_record = (
            await crud.get_congress_member_sponsorship_record(
                db, bioguide_id=bioguide_id
            )
        )

        logger.debug(db_congress_member_sponsorship_record.json())
        # db_congress_member_terms = await crud.get_congress_member_terms(db, bioguide_id=bioguide_id)

        if db_congress_member is None:
            logger.info(f"CongressMember not found for bioguide_id: {bioguide_id}")
            raise HTTPException(status_code=404, detail="CongressMember not found")

        # # Convert to Pydantic model
        result = CongressMemberSchema.from_orm(db_congress_member)
        # Cache the result
        await redis.set(bioguide_id, result.json(), expire=3600)
        logger.debug(f"Cache set for {bioguide_id}")

        return result.model_dump(by_alias=True)

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(
            f"Error fetching congress member with bioguide_id {bioguide_id}: {e}"
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")
