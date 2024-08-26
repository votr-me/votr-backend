import strawberry
from typing import List, Optional
import logging
from app.services import CongressMemberService
from app.graphql.types.congress_member import (
    CongressMemberDetails,
    CongressMember,
    CongressMemberTerms,
    CongressMemberSponsoredBills,
)
from fastapi import HTTPException

from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")


@strawberry.type
class Query:
    @strawberry.field
    async def get_congress_members_info(
        self, bioguide_ids: List[str], info
    ) -> List[Optional[CongressMemberDetails]]:
        if not bioguide_ids:
            logger.warning("No bioguide_ids provided.")
            raise HTTPException(status_code=400, detail="No bioguide_ids provided")

        # Initialize the CongressMemberService
        service = CongressMemberService(
            db=info.context["db"], redis=info.context["redis"]
        )

        results = []
        try:
            for bioguide_id in bioguide_ids:
                # Fetch congress member info using the service
                result_data = await service.get_congress_member_info(bioguide_id)

                # Transform the result data into the expected GraphQL type
                member_details = CongressMemberDetails(
                    congress_member=CongressMember(**result_data["congress_member"]),
                    terms=[
                        CongressMemberTerms(**term) for term in result_data["terms"]
                    ],
                    sponsored_bills=[
                        CongressMemberSponsoredBills(**bill)
                        for bill in result_data["sponsored_bills"]
                    ],
                )
                results.append(member_details)
        except HTTPException as e:
            raise e
        except Exception as e:
            logger.error(
                f"Error fetching congress members with bioguide_ids {bioguide_ids}: {str(e)}"
            )
            raise HTTPException(status_code=500, detail="Internal Server Error")

        return results
