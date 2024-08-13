import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

import json
from app.core.logging_config import configure_logging
from app.db.session import get_db
from app.core.redis import get_redis_pool, RedisPool
from app.db.crud.crud_acs5 import ACS5CRUD
from app.schemas.census.acs5 import (
    ACS5DemographicsSchema,
    ACS5EmploymentSchema,
    ACS5IncomeSchema,
)
from .constants import *
from fastapi.encoders import jsonable_encoder

configure_logging()
logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/demographics/",
)
async def read_acs5_demographics_data(
    state_fips: str = Query(..., description="State FIPS code"),
    district_num: str = Query(..., description="District number"),
    db: AsyncSession = Depends(get_db),
    redis: RedisPool = Depends(get_redis_pool),
):
    if not state_fips in VALID_STATE_FIPS_CODES:
        logger.warning("Invalid state_fips provided.")
        raise HTTPException(status_code=400, detail="Invalid state FIPS")
    else:
        if not district_num in VALID_CONGRESSIONAL_DISTRICTS_BY_STATE_FIPS.get(
            state_fips, {}
        ):
            logger.debug(
                f"District {district_num} does not exist for State FIPS code {state_fips}"
            )

        else:
            logger.debug(
                f"Fetching data for congressionl district {district_num} in {state_fips}"
            )

    redis_key = f"{state_fips}_{district_num}_demographics"
    try:
        # Check if the result is in the cache
        cached_result = await redis.get(redis_key)

        if cached_result:
            logger.debug(f"Cache hit for {redis_key}")
            return JSONResponse(
                content=json.loads(cached_result), media_type="application/json"
            )

        state_district_demos_db = (
            await ACS5CRUD().get_congerssional_district_asc5_demographics(
                db=db, district_num=district_num, state_fip=state_fips
            )
        )

        if not state_district_demos_db:
            logger.info(f"No data found for {state_fips} district {district_num}")
            raise HTTPException(
                status_code=404,
                detail=f"No data found for {state_fips} district {district_num}",
            )

        # Convert to Pydantic model
        result = [
            ACS5DemographicsSchema.from_orm(record).model_dump(by_alias=True)
            for record in state_district_demos_db
        ]
        result_json = jsonable_encoder(result)
        # Cache the result
        await redis.set(redis_key, json.dumps(result_json), expire=3600)
        logger.debug(f"Cache set for {redis_key}")

        return result

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(
            f"Error fetching congress member with bioguide_id {redis_key}: {e}"
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get(
    "/employment/",
)
async def read_acs5_employment_data(
    state_fips: str = Query(..., description="State FIPS code"),
    district_num: str = Query(..., description="District number"),
    db: AsyncSession = Depends(get_db),
    redis: RedisPool = Depends(get_redis_pool),
):
    if not state_fips in VALID_STATE_FIPS_CODES:
        logger.warning("Invalid state_fips provided.")
        raise HTTPException(status_code=400, detail="Invalid state FIPS")
    else:
        if not district_num in VALID_CONGRESSIONAL_DISTRICTS_BY_STATE_FIPS.get(
            state_fips, {}
        ):
            logger.debug(
                f"District {district_num} does not exist for State FIPS code {state_fips}"
            )

        else:
            logger.debug(
                f"Fetching data for congressionl district {district_num} in {state_fips}"
            )

    redis_key = f"{state_fips}_{district_num}_employment"
    try:
        # Check if the result is in the cache
        cached_result = await redis.get(redis_key)

        if cached_result:
            logger.debug(f"Cache hit for {redis_key}")
            return JSONResponse(
                content=json.loads(cached_result), media_type="application/json"
            )

        state_district_employment_db = (
            await ACS5CRUD().get_congerssional_district_asc5_employment(
                db=db, district_num=district_num, state_fips=state_fips
            )
        )

        if not state_district_employment_db:
            logger.info(f"No data found for {state_fips} district {district_num}")
            raise HTTPException(
                status_code=404,
                detail=f"No data found for {state_fips} district {district_num}",
            )

        # Convert to Pydantic model
        result = [
            ACS5EmploymentSchema.from_orm(record).model_dump(by_alias=True)
            for record in state_district_employment_db
        ]
        result_json = jsonable_encoder(result)

        # Cache the result
        await redis.set(redis_key, json.dumps(result_json), expire=3600)
        logger.debug(f"Cache set for {redis_key}")

        return result

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(
            f"Error fetching congress member with bioguide_id {redis_key}: {e}"
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get(
    "/income/",
)
async def read_acs5_employment_data(
    state_fips: str = Query(..., description="State FIPS code"),
    district_num: str = Query(..., description="District number"),
    db: AsyncSession = Depends(get_db),
    redis: RedisPool = Depends(get_redis_pool),
):
    if not state_fips in VALID_STATE_FIPS_CODES:
        logger.warning("Invalid state_fips provided.")
        raise HTTPException(status_code=400, detail="Invalid state FIPS")
    else:
        if not district_num in VALID_CONGRESSIONAL_DISTRICTS_BY_STATE_FIPS.get(
            state_fips, {}
        ):
            logger.debug(
                f"District {district_num} does not exist for State FIPS code {state_fips}"
            )

        else:
            logger.debug(
                f"Fetching data for congressionl district {district_num} in {state_fips}"
            )

    redis_key = f"{state_fips}_{district_num}_income"
    try:
        # Check if the result is in the cache
        cached_result = await redis.get(redis_key)

        if cached_result:
            logger.debug(f"Cache hit for {redis_key}")
            return JSONResponse(
                content=json.loads(cached_result), media_type="application/json"
            )

        state_district_income_db = (
            await ACS5CRUD().get_congerssional_district_asc5_income(
                db=db, district_num=district_num, state_fips=state_fips
            )
        )

        if not state_district_income_db:
            logger.info(f"No data found for {state_fips} district {district_num}")
            raise HTTPException(
                status_code=404,
                detail=f"No data found for {state_fips} district {district_num}",
            )

        # Convert to Pydantic model
        result = [
            ACS5IncomeSchema.from_orm(record).model_dump(by_alias=True)
            for record in state_district_income_db
        ]
        result_json = jsonable_encoder(result)

        # Cache the result
        await redis.set(redis_key, json.dumps(result_json), expire=3600)
        logger.debug(f"Cache set for {redis_key}")

        return result

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(
            f"Error fetching congress member with bioguide_id {redis_key}: {e}"
        )
        raise HTTPException(status_code=500, detail="Internal Server Error")
