from app.db.crud.crud_acs5 import ACS5CRUD
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from app.core.redis import RedisPool
from .BaseService import BaseService
from typing import Dict, Any
from app.schemas.census.acs5 import *
from app.db.models.acs5 import *


from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")


class ACS5Service(BaseService):
    """Service for handling operations related to ACS5 data."""

    def __init__(
        self, db: AsyncSession, redis: RedisPool, district_num: str, state_fips: str
    ):
        super().__init__(
            db, redis, ACS5CRUD, district_num=district_num, state_fips=state_fips
        )

    async def get_acs5_data(self, model) -> Dict[str, Any]:
        data = await self.fetch_and_validate(
            self.crud.get_congressional_district_acs5_data,
            model,
            error_message=f"ACS5 data not found for state {self.crud.state_fips} congressional district {self.crud.district_num}",
        )
        return data

    async def fetch_acs5_info(self):
        db_acs5_cd_demographics = await self.get_acs5_data(ACS5Demographics)
        db_acs5_cd_income = await self.get_acs5_data(ACS5Income)
        db_acs5_cd_employment = await self.get_acs5_data(ACS5Employment)

        return self.transform_to_schema(
            db_acs5_cd_demographics, db_acs5_cd_employment, db_acs5_cd_income
        )

    def transform_to_schema(
        self, cd_demographics, cd_employment, cd_income
    ) -> Dict[str, Any]:
        cd_demographics_schema = [
            ACS5DemographicsSchema.model_validate(record) for record in cd_demographics
        ]
        cd_employment_schema = [
            ACS5EmploymentSchema.model_validate(record) for record in cd_employment
        ]
        cd_income_schema = [
            ACS5IncomeSchema.model_validate(record) for record in cd_income
        ]

        return {
            "cd_demographics": [
                record.model_dump() for record in cd_demographics_schema
            ],
            "cd_employment": [record.model_dump() for record in cd_employment_schema],
            "cd_income": [record.model_dump() for record in cd_income_schema],
        }
