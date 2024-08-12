from app.db.crud.crud_congress_member import CongressMemberCRUD
from app.db.models.congress_members import CongressMember
from app.schemas.congress.congress_members import (
    CongressMemberSchema,
    CongressMemberSponsoredBillsSchema,
    CongressMemberTermsSchema,
)
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from app.core.redis import RedisPool
from fastapi import HTTPException
from app.core.logging_config import configure_logging
from .BaseService import BaseService
from typing import Dict, Any
configure_logging()
logger = logging.getLogger(__name__)


class CongressMemberService(BaseService):
    """Service for handling operations related to Congress Members."""

    def __init__(self, db: AsyncSession, redis: RedisPool):
        super().__init__(db, redis, CongressMemberCRUD(CongressMember))

    async def get_congress_member_info(self, bioguide_id: str) -> Dict[str, Any]:
        """Fetch Congress member info, terms, and sponsored bills."""
        db_congress_member = await self.fetch_congress_member(bioguide_id)
        db_congress_member_terms = await self.fetch_congress_member_terms(bioguide_id)
        db_congress_member_sponsorship_record = await self.fetch_congress_member_sponsored_bills(bioguide_id)

        return self.transform_to_schema(
            db_congress_member, db_congress_member_terms, db_congress_member_sponsorship_record
        )

    async def fetch_congress_member(self, bioguide_id: str) -> CongressMember:
        """Fetch congress member from the database."""
        db_congress_member = await self.crud.get_by_bioguide_id(self.db, bioguide_id)
        if not db_congress_member:
            logger.info(f"CongressMember not found for bioguide_id: {bioguide_id}")
            raise HTTPException(status_code=404, detail="CongressMember not found")
        return db_congress_member

    async def fetch_congress_member_terms(self, bioguide_id: str) -> list:
        """Fetch congress member terms from the database."""
        return await self.crud.get_congress_member_terms(self.db, bioguide_id=bioguide_id)

    async def fetch_congress_member_sponsored_bills(self, bioguide_id: str) -> list:
        """Fetch congress member sponsored bills from the database."""
        return await self.crud.get_congress_member_sponsorship_record(self.db, bioguide_id=bioguide_id)

    def transform_to_schema(self, member, terms, sponsored_bills) -> Dict[str, Any]:
        """Transform database models to schema and prepare the final response."""
        congress_member_schema = CongressMemberSchema.model_validate(member)
        congress_member_terms_schema = [
            CongressMemberTermsSchema.model_validate(term) for term in terms
        ]
        congress_member_sponsored_bills_schema = [
            CongressMemberSponsoredBillsSchema.model_validate(bill) for bill in sponsored_bills
        ]

        return {
            "congress_member": congress_member_schema.model_dump(),
            "terms": [term.model_dump() for term in congress_member_terms_schema],
            "sponsored_bills": [bill.model_dump() for bill in congress_member_sponsored_bills_schema],
        }
