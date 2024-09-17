from fastapi import APIRouter

from app.api.v1.routes import voter_info_router, legislator_router


api_router = APIRouter()
api_router.include_router(voter_info_router, prefix="/voter_info", tags=["voter_info"])
api_router.include_router(legislator_router, prefix="/legislator", tags=["legislator"])
