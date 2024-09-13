from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.legislator_service import LegislatorService
from app.data.session import get_session
from app.data.repositories.legislator_repository import (
    LegislatorRepository,
    LegislatorTermsRepository,
    LegislatorSponsoredBillsRepository,
)


async def get_legislator_service(
    db: AsyncSession = Depends(get_session),
) -> LegislatorService:
    legislator_repo = LegislatorRepository(db)
    legislator_terms_repo = LegislatorTermsRepository(db)
    legislator_sponsored_bills_repo = LegislatorSponsoredBillsRepository(db)

    return LegislatorService(
        db=db,
        legislator_repo=legislator_repo,
        legislator_terms_repo=legislator_terms_repo,
        legislator_sponsored_bills_repo=legislator_sponsored_bills_repo,
    )
