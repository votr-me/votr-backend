from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.congress_members import (
    CongressMember,
    CongressMemberTerms,
    CongressMemberSponsoredBills,
)
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from typing import Optional


class CongressMemberCRUD:
    def __init__(self, db: AsyncSession):
        self.db = db

    """CRUD operations specific to CongressMember, if any."""

    async def get_by_bioguide_id(
        self, bioguide_id: str, load_relationships: bool = False
    ) -> Optional[CongressMember]:
        query = select(CongressMember).filter(CongressMember.bioguide_id == bioguide_id)
        if load_relationships:
            for relationship_name in CongressMember.__mapper__.relationships.keys():
                query = query.options(
                    selectinload(getattr(CongressMember, relationship_name))
                )
        result = await self.db.execute(query)

        return result.scalars().first()

    async def get_congress_member_terms(
        self, db: AsyncSession, bioguide_id: str
    ) -> Optional[CongressMemberTerms]:
        query = select(CongressMemberTerms).filter(
            CongressMemberTerms.bioguide_id == bioguide_id
        )

        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_congress_member_sponsorship_record(
        self, db: AsyncSession, bioguide_id: str
    ) -> Optional[CongressMemberSponsoredBills]:
        query = select(CongressMemberSponsoredBills).filter(
            CongressMemberSponsoredBills.bioguide_id == bioguide_id
        )

        result = await self.db.execute(query)
        return result.scalars().all()
