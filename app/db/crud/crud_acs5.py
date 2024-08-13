from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.acs5 import ACS5Demographics, ACS5Employment, ACS5Income
from sqlalchemy.future import select
from .crud_base import CRUDBase


class ACS5CRUD:
    async def get_congerssional_district_asc5_demographics(
        self, db: AsyncSession, district_num: int, state_fips: str
    ):
        query = (
            select(ACS5Demographics)
            .filter(ACS5Demographics.state_fip == state_fips)
            .filter(ACS5Demographics.congressional_district == district_num)
        )
        result = await db.execute(query)
        return result.scalars().all()

    async def get_congerssional_district_asc5_employment(
        self, db: AsyncSession, district_num: int, state_fips: str
    ):
        query = (
            select(ACS5Employment)
            .filter(ACS5Employment.state_fip == state_fips)
            .filter(ACS5Employment.congressional_district == district_num)
        )
        result = await db.execute(query)
        return result.scalars().all()

    async def get_congerssional_district_asc5_income(
        self, db: AsyncSession, district_num: int, state_fips: str
    ):
        query = (
            select(ACS5Income)
            .filter(ACS5Income.state_fip == state_fips)
            .filter(ACS5Income.congressional_district == district_num)
        )
        result = await db.execute(query)
        return result.scalars().all()

    