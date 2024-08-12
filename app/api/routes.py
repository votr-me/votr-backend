from fastapi import APIRouter

from app.api.v1.routes import (
    voters_router,
    elections_router,
    legislators_router,
    census_router,
)


api_router = APIRouter()
api_router.include_router(voters_router, prefix="/voter_info", tags=["voter_info"])
api_router.include_router(elections_router, prefix="/elections", tags=["elections"])
api_router.include_router(
    legislators_router, prefix="/congress_members", tags=["congress_members"]
)
api_router.include_router(census_router, prefix="/census", tags=["census"])
