from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.crud_base import CRUDBase
from app.db.models.congress_members import CongressMember


class CRUDCongressMember(CRUDBase[CongressMember]):
    async def get_by_bioguide_id(self, db: AsyncSession, bioguide_id: str):
        query = select(self.model).filter(self.model.bioguide_id == bioguide_id)
        result = await db.execute(query)
        return result.scalars().first()


congress_member = CRUDCongressMember(CongressMember)
