from fastapi import APIRouter

from app.api.v1.routes import (
    voter_info_router,
)


api_router = APIRouter()
api_router.include_router(voter_info_router, prefix="/legislator", tags=["legislators"])
