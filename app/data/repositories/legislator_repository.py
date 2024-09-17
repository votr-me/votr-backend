from app.data.models.legislators import (
    Legislator,
    LegislatorSponsoredBills,
    LegislatorTerms,
)
from app.data.models.legislators import Legislator
from app.data.repositories.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from abc import ABC, abstractmethod


class LegislatorRepositoryInterface(ABC):
    @abstractmethod
    async def get_by_bioguide_id(self, bioguide_id: str) -> Optional[Legislator]:
        pass

    @abstractmethod
    async def get_current_legislators_by_state(
        self, state_abbrv: str
    ) -> List[Legislator]:
        pass

    @abstractmethod
    async def get_legislators_historical_by_state(
        self, state_abbrv: str
    ) -> List[Legislator]:
        pass


class LegislatorSponsoredBillsRepositoryInterface(ABC):
    @abstractmethod
    async def get_by_bioguide_id(
        self, bioguide_id: str
    ) -> List[LegislatorSponsoredBills]:
        pass


class LegislatorTermsRepositoryInterface(ABC):
    @abstractmethod
    async def get_by_bioguide_id(self, bioguide_id: str) -> List[LegislatorTerms]:
        pass


class LegislatorRepository(BaseRepository[Legislator], LegislatorRepositoryInterface):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Legislator)

    async def get_by_bioguide_id(self, bioguide_id: str) -> Optional[Legislator]:
        return await self.get_by_field("bioguide_id", bioguide_id)

    async def get_current_legislators_by_state(
        self, state_abbrv: str
    ) -> List[Legislator]:
        query = select(self.model).where(
            self.model.is_current_member.is_(True),
            self.model.member_state == state_abbrv.upper(),
        )
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_legislators_historical_by_state(
        self, state_abbrv: str
    ) -> List[Legislator]:
        return await self.get_all_by_field("member_state", state_abbrv.upper())


class LegislatorSponsoredBillsRepository(
    BaseRepository[LegislatorSponsoredBills],
    LegislatorSponsoredBillsRepositoryInterface,
):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LegislatorSponsoredBills)

    async def get_by_bioguide_id(
        self, bioguide_id: str
    ) -> List[LegislatorSponsoredBills]:
        return await self.get_all_by_field("bioguide_id", bioguide_id)


class LegislatorTermsRepository(
    BaseRepository[LegislatorTerms], LegislatorTermsRepositoryInterface
):
    def __init__(self, db: AsyncSession):
        super().__init__(db, LegislatorTerms)

    async def get_by_bioguide_id(self, bioguide_id: str) -> List[LegislatorTerms]:
        return await self.get_all_by_field("bioguide_id", bioguide_id)
