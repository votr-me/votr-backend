from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import LegislatorService, AddressService
from app.data.session import get_session
from app.data.repositories.legislator_repository import (
    LegislatorRepository,
    LegislatorTermsRepository,
    LegislatorSponsoredBillsRepository,
    LegislatorRepositoryInterface,
    LegislatorTermsRepositoryInterface,
    LegislatorSponsoredBillsRepositoryInterface,
)
from app.core.config import config
from app.data import GeocodioRepository
from app.core.redis import RedisPool, get_redis_pool


def get_legislator_repository(
    db: AsyncSession = Depends(get_session),
) -> LegislatorRepositoryInterface:
    return LegislatorRepository(db)


def get_bills_repository(
    db: AsyncSession = Depends(get_session),
) -> LegislatorSponsoredBillsRepositoryInterface:
    return LegislatorSponsoredBillsRepository(db)


def get_terms_repository(
    db: AsyncSession = Depends(get_session),
) -> LegislatorTermsRepositoryInterface:
    return LegislatorTermsRepository(db)


def get_legislator_service(
    legislator_repo: LegislatorRepositoryInterface = Depends(get_legislator_repository),
    bills_repo: LegislatorSponsoredBillsRepositoryInterface = Depends(
        get_bills_repository
    ),
    terms_repo: LegislatorTermsRepositoryInterface = Depends(get_terms_repository),
) -> LegislatorService:
    return LegislatorService(
        legislator_repo=legislator_repo,
        bills_repo=bills_repo,
        terms_repo=terms_repo,
    )


def get_geocodio_repo() -> GeocodioRepository:
    return GeocodioRepository(api_key=config.GEOCODIO_API_KEY)


def get_address_service(
    geocodio_repo: GeocodioRepository = Depends(get_geocodio_repo),
) -> AddressService:
    return AddressService(geocodio_repo=geocodio_repo)


async def get_context(
    db: AsyncSession = Depends(get_session),
    redis: RedisPool = Depends(get_redis_pool),
):
    legislator_service = LegislatorService(db=db)
    return {"db": db, "redis": redis, "legislator_service": legislator_service}
