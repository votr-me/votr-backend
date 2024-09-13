from app.data.models.legislators import (
    Legislator,
    LegislatorSponsoredBills,
    LegislatorTerms,
)
from app.data.repositories.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional


class LegislatorRepository(BaseRepository[Legislator]):
    """
    Repository for handling operations related to Legislator entities.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, Legislator)

    async def get_by_bioguide_id(self, bioguide_id: str) -> Optional[Legislator]:
        """
        Retrieve a Legislator by their bioguide ID.

        Args:
            bioguide_id (str): The bioguide ID of the legislator.

        Returns:
            Optional[Legislator]: The Legislator instance if found, None otherwise.
        """
        query = select(Legislator).filter(Legislator.bioguide_id == bioguide_id)
        result = await self.db.execute(query)
        member = result.scalars().one_or_none()

        if not member:
            # Log or handle cases where the member is not found
            # You could raise a custom exception if required
            return None

        return member

    async def get_current_legislators_by_state(
        self, state_abbrv: str
    ) -> List[Legislator]:
        """
        Retrieve all current Legislators from a given state.

        Args:
            state_abbrv (str): Two-letter state abbreviation (e.g., 'CA').

        Returns:
            List[Legislator]: A list of current legislators from the specified state.
        """
        query = select(Legislator).filter(
            Legislator.is_current_member.is_(True),
            Legislator.member_state == state_abbrv,
        )
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_legislators_historical_by_state(
        self, state_abbrv: str
    ) -> List[Legislator]:
        """
        Retrieve all legislators (historical and current) from a given state.

        Args:
            state_abbrv (str): Two-letter state abbreviation (e.g., 'CA').

        Returns:
            List[Legislator]: A list of legislators from the specified state.
        """
        query = select(Legislator).filter(Legislator.member_state == state_abbrv)
        result = await self.db.execute(query)
        return result.scalars().all()


class LegislatorSponsoredBillsRepository(BaseRepository[LegislatorSponsoredBills]):
    """
    Repository for handling operations related to LegislatorSponsoredBills entities.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, LegislatorSponsoredBills)

    async def get_legislator_sponsored_bills_by_bioguide_id(
        self, bioguide_id: str
    ) -> List[LegislatorSponsoredBills]:
        """
        Retrieve all sponsored bills for a legislator based on their bioguide ID.

        Args:
            bioguide_id (str): The bioguide ID of the legislator.

        Returns:
            List[LegislatorSponsoredBills]: A list of sponsored bills by the legislator.
        """
        query = select(LegislatorSponsoredBills).filter(
            LegislatorSponsoredBills.bioguide_id == bioguide_id
        )
        result = await self.db.execute(query)
        return result.scalars().all()


class LegislatorTermsRepository(BaseRepository[LegislatorTerms]):
    """
    Repository for handling operations related to LegislatorTerms entities.
    """

    def __init__(self, db: AsyncSession):
        super().__init__(db, LegislatorTerms)  # Fixed the incorrect model reference

    async def get_legislator_terms_all(self, bioguide_id: str) -> List[LegislatorTerms]:
        """
        Retrieve all terms served by a legislator based on their bioguide ID.

        Args:
            bioguide_id (str): The bioguide ID of the legislator.

        Returns:
            List[LegislatorTerms]: A list of terms served by the legislator.
        """
        query = select(LegislatorTerms).filter(
            LegislatorTerms.bioguide_id == bioguide_id
        )
        result = await self.db.execute(query)
        return result.scalars().all()
