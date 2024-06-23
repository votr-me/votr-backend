from app.api.v1.routes import voters_router, elections_router, legislators_router
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(voters_router, prefix="/voter_info", tags=["voter_info"])
api_router.include_router(elections_router, prefix="/elections", tags=["elections"])
api_router.include_router(
    legislators_router, prefix="/legislators", tags=["legislators"]
)
