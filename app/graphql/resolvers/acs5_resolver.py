import strawberry
from typing import Optional
import logging
from app.services import ACS5Service
from app.graphql.types.acs5 import *
from fastapi import HTTPException

from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")


@strawberry.type
class Query:
    @strawberry.field
    async def get_acs5_info(
        self, district_num: str, state_fips: str, info
    ) -> Optional[ACS5Details]:
        if not district_num:
            logger.warning("No district number provided.")
            raise HTTPException(status_code=400, detail="No district number provided")

        if not state_fips:
            logger.warning("No state FIPS code provided.")
            raise HTTPException(status_code=400, detail="No state FIPS code provided")

        # Initialize the ACS5Service with necessary parameters
        service = ACS5Service(
            db=info.context["db"],
            redis=info.context["redis"],
            district_num=district_num,
            state_fips=state_fips,
        )

        try:
            # Fetch the ACS5 info using the service layer
            result_data = await service.fetch_acs5_info()

            # Transform the result data into the expected GraphQL type
            acs5_details = ACS5Details(
                cd_demographics=[
                    ACS5Demographics(**record)
                    for record in result_data["cd_demographics"]
                ],
                cd_employment=[
                    ACS5Employment(**record) for record in result_data["cd_employment"]
                ],
                cd_income=[ACS5Income(**record) for record in result_data["cd_income"]],
            )
        except HTTPException as e:
            raise e
        except Exception as e:
            logger.error(
                f"Error fetching data for state {state_fips} congressional district {district_num}: {str(e)}"
            )
            raise HTTPException(status_code=500, detail="Internal Server Error")

        return acs5_details
