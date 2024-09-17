from app.data.repositories.legislator_repository import (
    LegislatorRepository,
    LegislatorSponsoredBillsRepository,
    LegislatorTermsRepository,
    LegislatorRepositoryInterface,
    LegislatorSponsoredBillsRepositoryInterface,
    LegislatorTermsRepositoryInterface,
)
from app.data.models.legislators import Legislator
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.services.base_service import BaseService


class LegislatorService:
    def __init__(
        self,
        legislator_repo: LegislatorRepositoryInterface,
        bills_repo: LegislatorSponsoredBillsRepositoryInterface,
        terms_repo: LegislatorTermsRepositoryInterface,
    ):
        self.legislator_repo = legislator_repo
        self.bills_repo = bills_repo
        self.terms_repo = terms_repo

    async def get_legislator_info(self, bioguide_id: str):
        legislator = await self.legislator_repo.get_by_bioguide_id(bioguide_id)
        if not legislator:
            # Handle legislator not found
            pass

        # bills = await self.bills_repo.get_by_bioguide_id(bioguide_id)
        # terms = await self.terms_repo.get_by_bioguide_id(bioguide_id)

        # Process and return the combined information
        return legislator
