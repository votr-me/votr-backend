from app.data.repositories.legislator_repository import (
    LegislatorRepository,
    LegislatorSponsoredBillsRepository,
    LegislatorTermsRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.services.base_service import BaseService


class LegislatorService:
    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db
        self.legislator_repo = LegislatorRepository(db=self.db)
        self.bills_repo = LegislatorSponsoredBillsRepository(db=self.db)
        self.terms_repo = LegislatorTermsRepository(db=self.db)

    async def get_legislator_info(self, bioguide_id: str):
        legislator = await self.legislator_repo.get_by_bioguide_id(bioguide_id)
        if not legislator:
            # Handle legislator not found
            return None

        bills = await self.bills_repo.get_by_bioguide_id(bioguide_id)
        terms = await self.terms_repo.get_by_bioguide_id(bioguide_id)

        legislator_info = {
            "legislator": legislator,
            "terms": terms,
            "sponsored_bills": bills,
        }
        # Process and return the combined information
        return legislator_info
