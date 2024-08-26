from fastapi import APIRouter

from app.api.v1.routes import (
    voters_router,
)


api_router = APIRouter()
api_router.include_router(voters_router, prefix="/voter_info", tags=["voter_info"])
