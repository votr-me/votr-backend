from app.schemas import (
    LegislatorSchema,
    LegislatorTermsSchema,
    LegislatorSponsoredBillsSchema,
)
import strawberry
from typing import List


@strawberry.experimental.pydantic.type(model=LegislatorSchema, all_fields=True)
class Legislator:
    pass


@strawberry.experimental.pydantic.type(model=LegislatorTermsSchema, all_fields=True)
class LegislatorTerms:
    pass


@strawberry.experimental.pydantic.type(
    model=LegislatorSponsoredBillsSchema, all_fields=True
)
class LegislatorSponsoredBills:
    pass


@strawberry.type
class LegislatorDetails:
    legislator: Legislator
    terms: List[LegislatorTerms]
    sponsored_bills: List[LegislatorSponsoredBills]
