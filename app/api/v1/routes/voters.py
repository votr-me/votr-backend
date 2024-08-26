import logging
from typing import List
from fastapi import APIRouter, HTTPException, Depends, Query, Request, Response
from app.core.dependencies import get_geocodio_client
from app.services import GeocodioAsyncAPIClient
from app.db.crud.crud_congress_member import CongressMemberCRUD
from app.schemas.congress.congress_members import CongressMemberSchema
from app.db.session import get_session
from sqlalchemy.ext.asyncio import AsyncSession
import json
from app.core.logging_config import configure_logging

router = APIRouter()


configure_logging()
logger = logging.getLogger("app")


@router.get(
    "/my_legislators",
    status_code=200,
)
async def get_user_location_info(
    request: Request,
    response: Response,
    session: AsyncSession = Depends(get_session),
    client: GeocodioAsyncAPIClient = Depends(get_geocodio_client),
    address: str = Query(..., description="The address to geolocate"),
    fields: List[str] = Query(
        default=["cd"],
        description="List of fields to return from geocodio API (e.g. stateleg, cd)",
    ),
) -> List[CongressMemberSchema]:
    try:
        response.set_cookie(
            key="user_address", value=address, httponly=True, secure=True
        )
        geolocation_data = await client.geolocate(
            address=address,
            fields=fields,
        )

        if not geolocation_data:
            raise HTTPException(status_code=404, detail="No results found")

        response.set_cookie(
            key="user_geolocation",
            value=str(geolocation_data),
            httponly=True,
            secure=True,
        )

        if geolocation_data:
            _legislators = []
            for id in geolocation_data.get("bioguide_ids", []):
                _legislator = await CongressMemberCRUD(db=session).get_by_bioguide_id(
                    bioguide_id=id
                )
                if _legislator:
                    if isinstance(_legislator.leadership_type, dict):
                        _legislator.leadership_type = transform_leadership_type(
                            _legislator.leadership_type
                        )
                    legislator_schema = CongressMemberSchema.from_orm(_legislator)
                    _legislators.append(legislator_schema)

            if len(_legislators) == 0:
                raise HTTPException(
                    status_code=500,
                    detail=f'No Legislators found for {geolocation_data.get("address", None)}',
                )

            if _legislators:
                # Serialize Pydantic models to JSON
                serialized_legislators = json.dumps(
                    [legislator.dict() for legislator in _legislators]
                )

                # Store the serialized legislators data in a cookie
                response.set_cookie(
                    key="legislators",
                    value=serialized_legislators,
                    httponly=True,
                    secure=True,
                )
            return _legislators

    except HTTPException as e:
        logger.error(f"Geolocation error for address '{address}': {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error for address '{address}': {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
