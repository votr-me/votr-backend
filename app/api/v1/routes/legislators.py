import logging
from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_legislator_service
from app.services import LegislatorService

logger = logging.getLogger("app")
router = APIRouter()


@router.get("/{bioguide_id}")
# @cache(expire=config.DEFAULT_TTL)
async def get_legislator(
    bioguide_id: str, service: LegislatorService = Depends(get_legislator_service)
):
    """
    API route to get a congress member with their details.

    Args:
        bioguide_id (str): The bioguide ID of the congress member.

    Returns:
        A congress member with their terms and sponsored bills.
    """
    member = await service.get_legislator_info(bioguide_id)
    if not member:
        raise HTTPException(status_code=404, detail="Congress member not found")

    return member
