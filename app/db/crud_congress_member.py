from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.db.models.congress_members import (
    CongressMember,CongressMemberTerms, CongressMemberSponsoredBills
)
from sqlalchemy.future import select
from .crud_base import CRUDBase

class CongressMemberCRUD(CRUDBase[CongressMember]):
    """CRUD operations specific to CongressMember, if any."""
    
    async def get_congress_member_terms(self, db: AsyncSession, bioguide_id: str):
        query = select(CongressMemberTerms).filter(
            CongressMemberTerms.bioguide_id == bioguide_id
        )
        
        result = await db.execute(query)
        return result.scalars().first()
    
    async def get_congress_member_sponsorship_record(self, db: AsyncSession, bioguide_id: str):
        query = select(CongressMemberSponsoredBills).filter(
            CongressMemberSponsoredBills.bioguide_id == bioguide_id
        )
        
        result = await db.execute(query)
        return result.scalars().first()

