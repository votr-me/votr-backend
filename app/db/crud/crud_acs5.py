from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class ACS5CRUD:
    def __init__(self, db: AsyncSession, district_num: str, state_fips: str):
        self.db = db
        self.district_num = district_num
        self.state_fips = state_fips

    async def fetch_data(self, model, filters=None):
        query = select(model)
        if filters:
            for filter_condition in filters:
                query = query.filter(filter_condition)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_congressional_district_acs5_data(self, model):
        filters = [
            model.state_fip == self.state_fips,
            model.congressional_district == self.district_num,
        ]
        return await self.fetch_data(model, filters)

    async def get_state_acs5_data(self, model):
        filters = [model.state_fip == self.state_fips]
        return await self.fetch_data(model, filters)

    async def get_country_acs5_data(self, model):
        return await self.fetch_data(model)
