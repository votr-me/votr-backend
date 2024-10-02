# app/graphql/resolvers/legislator_resolver.py

import strawberry
from typing import List, Optional
import logging
from app.graphql.types.legislator_graphql_types import (
    LegislatorDetails,
    Legislator,
    LegislatorTerms,
    LegislatorSponsoredBills,
    LegislatorLeadership
)
from strawberry.types import Info
from app.core.utilities import object_as_dict

logger = logging.getLogger("app")


@strawberry.type
class Query:
    @strawberry.field
    async def get_legislators_info(
        self,
        bioguide_ids: List[str],
        info: Info,
    ) -> List[Optional[LegislatorDetails]]:
        if not bioguide_ids:
            logger.warning("No bioguide_ids provided.")
            raise ValueError("No bioguide_ids provided")

        legislator_service = info.context["legislator_service"]

        results = []
        try:
            for bioguide_id in bioguide_ids:
                result_data = await legislator_service.get_legislator_info(bioguide_id)

                if not result_data:
                    logger.warning(f"No data found for bioguide_id {bioguide_id}")
                    results.append(None)
                    continue

                leadership = result_data.get('legislator').__dict__.get('leadership_type')                
                legislator_dict = {key: value for key, value in object_as_dict(result_data["legislator"]).items() if key != 'leadership_type'}
                terms_list = [object_as_dict(term) for term in result_data["terms"]]
                bills_list = [
                    object_as_dict(bill) for bill in result_data["sponsored_bills"]
                ]
                leadership_list = []
                
                if leadership:
                    for position in leadership:
                        key, value = next(iter(position.items()))  # Get the first key-value pair
                        transformed_leadership = {"congress": key, "role": value}
                        leadership_list.append(transformed_leadership)
                logger.debug(leadership_list)
                member_details = LegislatorDetails(
                    legislator=Legislator(**legislator_dict),
                    terms=[LegislatorTerms(**term) for term in terms_list],
                    sponsored_bills=[
                        LegislatorSponsoredBills(**bill) for bill in bills_list
                    ],
                    leadership=[LegislatorLeadership(**position) for position in leadership_list]
                )
                results.append(member_details)
        except Exception as e:
            logger.error(
                f"Error fetching congress members with bioguide_ids {bioguide_ids}: {str(e)}"
            )
            raise ValueError("Internal Server Error")

        return results
