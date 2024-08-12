from app.schemas import ACS5IncomeSchema, ACS5EmploymentSchema, ACS5DemographicsSchema
import strawberry
from typing import List


class CongressMemberSponsoredBills:
    pass


@strawberry.experimental.pydantic.type(model=ACS5DemographicsSchema, all_fields=True)
class ACS5Demographics:
    pass


@strawberry.experimental.pydantic.type(model=ACS5EmploymentSchema, all_fields=True)
class ACS5Employment:
    pass


@strawberry.experimental.pydantic.type(model=ACS5IncomeSchema, all_fields=True)
class ACS5Income:
    pass


@strawberry.type
class ACS5CensusDetails:
    ACS5Demographics: ACS5Demographics
    ACS5Income: List[ACS5Income]
    ACS5Employment: List[ACS5Employment]
