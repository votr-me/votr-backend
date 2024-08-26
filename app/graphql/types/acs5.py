from app.schemas.census.acs5 import (
    ACS5IncomeSchema,
    ACS5EmploymentSchema,
    ACS5DemographicsSchema,
    ACS5CountryDemographicsSchema,
    ACS5CountryEmploymentSchema,
    ACS5CountryIncomeSchema,
    ACS5StateDemographicsSchema,
    ACS5StateEmploymentSchema,
    ACS5StateIncomeSchema,
)
import strawberry
from typing import List


@strawberry.experimental.pydantic.type(model=ACS5DemographicsSchema, all_fields=True)
class ACS5Demographics:
    pass


@strawberry.experimental.pydantic.type(model=ACS5EmploymentSchema, all_fields=True)
class ACS5Employment:
    pass


@strawberry.experimental.pydantic.type(model=ACS5IncomeSchema, all_fields=True)
class ACS5Income:
    pass


@strawberry.experimental.pydantic.type(
    model=ACS5CountryDemographicsSchema, all_fields=True
)
class ACS5CountryDemographics:
    pass


@strawberry.experimental.pydantic.type(model=ACS5CountryIncomeSchema, all_fields=True)
class ACS5CountryIncome:
    pass


@strawberry.experimental.pydantic.type(
    model=ACS5CountryEmploymentSchema, all_fields=True
)
class ACS5CountryEmployment:
    pass


@strawberry.experimental.pydantic.type(
    model=ACS5StateDemographicsSchema, all_fields=True
)
class ACS5StateDemographics:
    pass


@strawberry.experimental.pydantic.type(model=ACS5StateEmploymentSchema, all_fields=True)
class ACS5StateEmployment:
    pass


@strawberry.experimental.pydantic.type(model=ACS5StateIncomeSchema, all_fields=True)
class ACS5StateIncome:
    pass


@strawberry.type
class ACS5Details:
    cd_demographics: List[ACS5Demographics]
    cd_income: List[ACS5Income]
    cd_employment: List[ACS5Employment]
    # country_demographics: List[ACS5CountryDemographics]
    # country_income: List[ACS5CountryIncome]
    # country_employment: List[ACS5CountryEmployment]
    # state_employment: List[ACS5StateEmployment]
    # state_demographics: List[ACS5StateDemographics]
    # state_income: List[ACS5StateIncome]
