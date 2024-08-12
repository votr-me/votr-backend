from app.schemas import (
    CongressMemberSchema,
    CongressMemberTermsSchema,
    CongressMemberSponsoredBillsSchema,
)
import strawberry
from typing import List


@strawberry.experimental.pydantic.type(model=CongressMemberSchema, all_fields=True)
class CongressMember:
    pass


@strawberry.experimental.pydantic.type(model=CongressMemberTermsSchema, all_fields=True)
class CongressMemberTerms:
    pass


@strawberry.experimental.pydantic.type(
    model=CongressMemberSponsoredBillsSchema, all_fields=True
)
class CongressMemberSponsoredBills:
    pass


@strawberry.type
class CongressMemberDetails:
    congress_member: CongressMember
    terms: List[CongressMemberTerms]
    sponsored_bills: List[CongressMemberSponsoredBills]
