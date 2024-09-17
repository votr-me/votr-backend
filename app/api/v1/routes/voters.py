import logging
from fastapi import APIRouter, Depends, HTTPException
from app.services import AddressService
from app.dependencies import get_address_service
import us
from app.schemas import VoterInfo

logger = logging.getLogger("app")
router = APIRouter()


@router.get("/address_info")
# @cache(expire=config.DEFAULT_TTL)
async def get_address_info(
    address: str, service: AddressService = Depends(get_address_service)
):
    """
    API route to get a address' congressional district details.

    Args:
        address (str): the address to search info for.

    Returns:
        A congress member with their terms and sponsored bills.
    """
    # logger.debug(address)
    address_info = await service.get_address_details(address)
    if not address_info:
        raise HTTPException(status_code=404, detail="No address information found")

    results = address_info.get("results")
    if not results:
        raise HTTPException(status_code=404, detail="No results found for the address")

    first_result = results[0]
    formatted_address = first_result.get("formatted_address")
    address_components = first_result.get("address_components", {})
    state = address_components.get("state")
    

    if not state:
        raise HTTPException(status_code=404, detail="State information not found")

    state_fips = us.states.lookup(state).fips if us.states.lookup(state) else None
    if not state_fips:
        raise HTTPException(status_code=404, detail="Invalid state code")

    fields = first_result.get("fields", {})
    congressional_districts = fields.get("congressional_districts")
    if not congressional_districts:
        raise HTTPException(
            status_code=404, detail="No congressional district information found"
        )

    district_info = congressional_districts[0]
    district_name = district_info.get("name")
    district_number = str(district_info.get("district_number", "")).rjust(2, "0")

    current_legislators = district_info.get("current_legislators", [])
    legislators = [
        legislator.get("references", {}).get("bioguide_id")
        for legislator in current_legislators
    ]
        
    voter_info = VoterInfo(
        state=state,
        state_fips=state_fips,
        address=formatted_address,
        district_name=district_name,
        district_number=district_number,
        bioguide_ids=legislators,
    )

    return voter_info
