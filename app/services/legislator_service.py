from app.data.repositories.legislator_repository import (
    LegislatorRepository,
    LegislatorSponsoredBillsRepository,
    LegislatorTermsRepository,
)
from app.data.models.legislators import Legislator
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.services.base_service import BaseService


class LegislatorService(BaseService[Legislator]):
    """
    Service layer for managing Congress members, sponsored bills, and terms.
    Inherits shared functionality from BaseService.
    """

    def __init__(
        self,
        db: AsyncSession,
        legislator_repo: LegislatorRepository,
        legislator_terms_repo: LegislatorTermsRepository,
        legislator_sponsored_bills_repo: LegislatorSponsoredBillsRepository,
    ):
        super().__init__(db)
        self.legislator_repo = legislator_repo
        self.legislator_terms_repo = legislator_terms_repo
        self.legislator_sponsored_bills_repo = legislator_sponsored_bills_repo

    async def get_member_with_details(self, bioguide_id: str) -> Optional[Legislator]:
        """
        Get a Congress member along with their terms and sponsored bills.
        Logs the operation.

        Args:
            bioguide_id (str): The bioguide ID of the congress member.

        Returns:
            Optional[Legislator]: A Legislator object with details, or None if not found.
        """
        self.log_info(f"Fetching member details for bioguide_id: {bioguide_id}")
        member = await self.legislator_repo.get_by_bioguide_id(bioguide_id)
        if not member:
            self.log_error(f"Congress member with bioguide_id {bioguide_id} not found.")
            return None

        # member.terms = await self.legislator_terms_repo.get_legislator_terms_all(bioguide_id)
        # member.sponsored_bills = await self.legislator_sponsored_bills_repo.get_legislator_sponsored_bills_by_bioguide_id(bioguide_id)
        return member
