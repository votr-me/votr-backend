from app.schemas.congress import CongressMember, CongressMemberTerms, CongressMemberSponsoredBills
# from app.db.models.acs5 import ACS5Demographics, ACS5Employment, ACS5Income
import strawberry
from typing import List

@strawberry.experimental.pydantic.type(model=CongressMember, all_fields=True)
class CongressMember:
    pass

@strawberry.experimental.pydantic.type(model=CongressMemberTerms, all_fields=True)
class CongressMemberTerms:
    pass

@strawberry.experimental.pydantic.type(model=CongressMemberSponsoredBills, all_fields=True)
class CongressMemberSponsoredBills:
    pass

# @strawberry.experimental.pydantic.type(model=ACS5Demographics, all_fields=True)
# class ACS5Demographics:
#     pass

# @strawberry.experimental.pydantic.type(model=ACS5Employment, all_fields=True)
# class ACS5Employment:
#     pass

# @strawberry.experimental.pydantic.type(model=ACS5Income, all_fields=True)
# class ACS5Income:
#     pass

@strawberry.type
class CongressMemberDetails:
    congress_member: CongressMember
    terms: List[CongressMemberTerms]
    sponsored_bills: List[CongressMemberSponsoredBills]
    # demographics: ACS5Demographics
    # employment: ACS5Employment
    # income: ACS5Income