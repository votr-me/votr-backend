from pydantic import BaseModel, Field
from typing import Optional


class ACS5DemographicsSchema(BaseModel):
    year: Optional[int] = Field(None, description="Year of the data")
    state_fip: Optional[str] = Field(None, description="State FIPS code")
    congressional_district: Optional[str] = Field(
        None, description="Congressional district"
    )
    country: Optional[str] = Field(None, description="Country")

    cd_sex_total: Optional[int] = Field(
        None, description="Total sex count in the congressional district"
    )
    cd_pct_male: Optional[float] = Field(
        None, description="Percentage of males in the congressional district"
    )
    cd_sex_male: Optional[int] = Field(
        None, description="Total male count in the congressional district"
    )
    cd_pct_female: Optional[float] = Field(
        None, description="Percentage of females in the congressional district"
    )
    cd_total_voting_age: Optional[float] = Field(
        None, description="Total voting age population in the congressional district"
    )
    cd_pct_population_of_voting_age: Optional[float] = Field(
        None,
        description="Percentage of population of voting age in the congressional district",
    )

    cd_race_white_total: Optional[int] = Field(
        None, description="Total white race count in the congressional district"
    )
    cd_pct_white: Optional[float] = Field(
        None, description="Percentage of white race in the congressional district"
    )
    cd_asian_total: Optional[int] = Field(
        None, description="Total Asian race count in the congressional district"
    )
    cd_pct_asian: Optional[float] = Field(
        None, description="Percentage of Asian race in the congressional district"
    )
    cd_race_black_total: Optional[int] = Field(
        None, description="Total black race count in the congressional district"
    )
    cd_pct_black: Optional[float] = Field(
        None, description="Percentage of black race in the congressional district"
    )
    cd_race_hispanic_total: Optional[int] = Field(
        None, description="Total Hispanic race count in the congressional district"
    )
    cd_pct_hispanic: Optional[float] = Field(
        None, description="Percentage of Hispanic race in the congressional district"
    )
    cd_race_pacific_islander_total: Optional[int] = Field(
        None,
        description="Total Pacific Islander race count in the congressional district",
    )
    cd_pct_pacific_islander: Optional[float] = Field(
        None,
        description="Percentage of Pacific Islander race in the congressional district",
    )
    cd_race_other_total: Optional[int] = Field(
        None, description="Total other race count in the congressional district"
    )
    cd_pct_other_race: Optional[float] = Field(
        None, description="Percentage of other race in the congressional district"
    )
    cd_race_two_or_more_total: Optional[int] = Field(
        None, description="Total two or more races count in the congressional district"
    )
    cd_pct_two_or_more: Optional[float] = Field(
        None,
        description="Percentage of two or more races in the congressional district",
    )

    state_sex_total: Optional[int] = Field(
        None, description="Total sex count in the state"
    )
    state_pct_male: Optional[float] = Field(
        None, description="Percentage of males in the state"
    )
    state_sex_male: Optional[int] = Field(
        None, description="Total male count in the state"
    )
    state_pct_female: Optional[float] = Field(
        None, description="Percentage of females in the state"
    )
    state_total_voting_age: Optional[float] = Field(
        None, description="Total voting age population in the state"
    )
    state_pct_population_of_voting_age: Optional[float] = Field(
        None, description="Percentage of population of voting age in the state"
    )

    state_race_white_total: Optional[int] = Field(
        None, description="Total white race count in the state"
    )
    state_pct_white: Optional[float] = Field(
        None, description="Percentage of white race in the state"
    )
    state_asian_total: Optional[int] = Field(
        None, description="Total Asian race count in the state"
    )
    state_pct_asian: Optional[float] = Field(
        None, description="Percentage of Asian race in the state"
    )
    state_race_black_total: Optional[int] = Field(
        None, description="Total black race count in the state"
    )
    state_pct_black: Optional[float] = Field(
        None, description="Percentage of black race in the state"
    )
    state_race_hispanic_total: Optional[int] = Field(
        None, description="Total Hispanic race count in the state"
    )
    state_pct_hispanic: Optional[float] = Field(
        None, description="Percentage of Hispanic race in the state"
    )
    state_race_pacific_islander_total: Optional[int] = Field(
        None, description="Total Pacific Islander race count in the state"
    )
    state_pct_pacific_islander: Optional[float] = Field(
        None, description="Percentage of Pacific Islander race in the state"
    )
    state_race_other_total: Optional[int] = Field(
        None, description="Total other race count in the state"
    )
    state_pct_other_race: Optional[float] = Field(
        None, description="Percentage of other race in the state"
    )
    state_race_two_or_more_total: Optional[int] = Field(
        None, description="Total two or more races count in the state"
    )
    state_pct_two_or_more: Optional[float] = Field(
        None, description="Percentage of two or more races in the state"
    )

    us_sex_total: Optional[int] = Field(None, description="Total sex count in the US")
    us_pct_male: Optional[float] = Field(
        None, description="Percentage of males in the US"
    )
    us_sex_male: Optional[int] = Field(None, description="Total male count in the US")
    us_pct_female: Optional[float] = Field(
        None, description="Percentage of females in the US"
    )
    us_total_voting_age: Optional[float] = Field(
        None, description="Total voting age population in the US"
    )
    us_pct_population_of_voting_age: Optional[float] = Field(
        None, description="Percentage of population of voting age in the US"
    )

    us_race_white_total: Optional[int] = Field(
        None, description="Total white race count in the US"
    )
    us_pct_white: Optional[float] = Field(
        None, description="Percentage of white race in the US"
    )
    us_asian_total: Optional[int] = Field(
        None, description="Total Asian race count in the US"
    )
    us_pct_asian: Optional[float] = Field(
        None, description="Percentage of Asian race in the US"
    )
    us_race_black_total: Optional[int] = Field(
        None, description="Total black race count in the US"
    )
    us_pct_black: Optional[float] = Field(
        None, description="Percentage of black race in the US"
    )
    us_race_hispanic_total: Optional[int] = Field(
        None, description="Total Hispanic race count in the US"
    )
    us_pct_hispanic: Optional[float] = Field(
        None, description="Percentage of Hispanic race in the US"
    )
    us_race_pacific_islander_total: Optional[int] = Field(
        None, description="Total Pacific Islander race count in the US"
    )
    us_pct_pacific_islander: Optional[float] = Field(
        None, description="Percentage of Pacific Islander race in the US"
    )
    us_race_other_total: Optional[int] = Field(
        None, description="Total other race count in the US"
    )
    us_pct_other_race: Optional[float] = Field(
        None, description="Percentage of other race in the US"
    )
    us_race_two_or_more_total: Optional[int] = Field(
        None, description="Total two or more races count in the US"
    )
    us_pct_two_or_more: Optional[float] = Field(
        None, description="Percentage of two or more races in the US"
    )

    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5EmploymentSchema(BaseModel):
    year: Optional[int] = Field(None, description="Year of the data")
    state_fip: Optional[str] = Field(None, description="State FIPS code")
    congressional_district: Optional[str] = Field(
        None, description="Congressional district"
    )
    country: Optional[str] = Field(None, description="Country")

    cd_employment_status_total: Optional[float] = Field(
        None, description="Total employment status in the congressional district"
    )
    cd_in_labor_force: Optional[float] = Field(
        None, description="Total in labor force in the congressional district"
    )
    cd_pct_in_labor_force: Optional[float] = Field(
        None, description="Percentage in labor force in the congressional district"
    )
    cd_not_in_labor_force: Optional[float] = Field(
        None, description="Total not in labor force in the congressional district"
    )
    cd_pct_not_in_labor_force: Optional[float] = Field(
        None, description="Percentage not in labor force in the congressional district"
    )
    cd_civilian_labor_force: Optional[float] = Field(
        None, description="Total civilian labor force in the congressional district"
    )
    cd_pct_civilian_labor_force: Optional[float] = Field(
        None,
        description="Percentage of civilian labor force in the congressional district",
    )
    cd_civilian_employed: Optional[float] = Field(
        None, description="Total civilian employed in the congressional district"
    )
    cd_pct_civilian_employed: Optional[float] = Field(
        None,
        description="Percentage of civilian employed in the congressional district",
    )

    state_employment_status_total: Optional[float] = Field(
        None, description="Total employment status in the state"
    )
    state_in_labor_force: Optional[float] = Field(
        None, description="Total in labor force in the state"
    )
    state_pct_in_labor_force: Optional[float] = Field(
        None, description="Percentage in labor force in the state"
    )
    state_not_in_labor_force: Optional[float] = Field(
        None, description="Total not in labor force in the state"
    )
    state_pct_not_in_labor_force: Optional[float] = Field(
        None, description="Percentage not in labor force in the state"
    )
    state_civilian_labor_force: Optional[float] = Field(
        None, description="Total civilian labor force in the state"
    )
    state_pct_civilian_labor_force: Optional[float] = Field(
        None, description="Percentage of civilian labor force in the state"
    )
    state_civilian_employed: Optional[float] = Field(
        None, description="Total civilian employed in the state"
    )
    state_pct_civilian_employed: Optional[float] = Field(
        None, description="Percentage of civilian employed in the state"
    )

    us_employment_status_total: Optional[float] = Field(
        None, description="Total employment status in the US"
    )
    us_in_labor_force: Optional[float] = Field(
        None, description="Total in labor force in the US"
    )
    us_pct_in_labor_force: Optional[float] = Field(
        None, description="Percentage in labor force in the US"
    )
    us_not_in_labor_force: Optional[float] = Field(
        None, description="Total not in labor force in the US"
    )
    us_pct_not_in_labor_force: Optional[float] = Field(
        None, description="Percentage not in labor force in the US"
    )
    us_civilian_labor_force: Optional[float] = Field(
        None, description="Total civilian labor force in the US"
    )
    us_pct_civilian_labor_force: Optional[float] = Field(
        None, description="Percentage of civilian labor force in the US"
    )
    us_civilian_employed: Optional[float] = Field(
        None, description="Total civilian employed in the US"
    )
    us_pct_civilian_employed: Optional[float] = Field(
        None, description="Percentage of civilian employed in the US"
    )

    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5IncomeSchema(BaseModel):
    year: Optional[int] = Field(None, description="Year of the data")
    congressional_district: Optional[str] = Field(
        None, description="Congressional district"
    )
    state_fip: Optional[str] = Field(None, description="State FIPS code")
    cd_country: Optional[str] = Field(None, description="Country")

    cd_hh_income_total: Optional[float] = Field(
        None, description="Total household income in the congressional district"
    )
    cd_pct_hh_income_total: Optional[float] = Field(
        None,
        description="Percentage of total household income in the congressional district",
    )
    cd_hh_income_less_10k: Optional[float] = Field(
        None,
        description="Household income less than $10k in the congressional district",
    )
    cd_pct_hh_income_less_10k: Optional[float] = Field(
        None,
        description="Percentage of household income less than $10k in the congressional district",
    )
    cd_hh_income_10k_to_14k: Optional[float] = Field(
        None,
        description="Household income from $10k to $14k in the congressional district",
    )
    cd_pct_hh_income_10k_to_14k: Optional[float] = Field(
        None,
        description="Percentage of household income from $10k to $14k in the congressional district",
    )
    cd_hh_income_15k_to_19k: Optional[float] = Field(
        None,
        description="Household income from $15k to $19k in the congressional district",
    )
    cd_pct_hh_income_15k_to_19k: Optional[float] = Field(
        None,
        description="Percentage of household income from $15k to $19k in the congressional district",
    )
    cd_hh_income_20k_to_24k: Optional[float] = Field(
        None,
        description="Household income from $20k to $24k in the congressional district",
    )
    cd_pct_hh_income_20k_to_24k: Optional[float] = Field(
        None,
        description="Percentage of household income from $20k to $24k in the congressional district",
    )
    cd_hh_income_25k_to_29k: Optional[float] = Field(
        None,
        description="Household income from $25k to $29k in the congressional district",
    )
    cd_pct_hh_income_25k_to_29k: Optional[float] = Field(
        None,
        description="Percentage of household income from $25k to $29k in the congressional district",
    )
    cd_hh_income_30k_to_34k: Optional[float] = Field(
        None,
        description="Household income from $30k to $34k in the congressional district",
    )
    cd_pct_hh_income_30k_to_34k: Optional[float] = Field(
        None,
        description="Percentage of household income from $30k to $34k in the congressional district",
    )
    cd_hh_income_35k_to_39k: Optional[float] = Field(
        None,
        description="Household income from $35k to $39k in the congressional district",
    )
    cd_pct_hh_income_35k_to_39k: Optional[float] = Field(
        None,
        description="Percentage of household income from $35k to $39k in the congressional district",
    )
    cd_hh_income_40k_to_44k: Optional[float] = Field(
        None,
        description="Household income from $40k to $44k in the congressional district",
    )
    cd_pct_hh_income_40k_to_44k: Optional[float] = Field(
        None,
        description="Percentage of household income from $40k to $44k in the congressional district",
    )
    cd_hh_income_45k_to_49k: Optional[float] = Field(
        None,
        description="Household income from $45k to $49k in the congressional district",
    )
    cd_pct_hh_income_45k_to_49k: Optional[float] = Field(
        None,
        description="Percentage of household income from $45k to $49k in the congressional district",
    )
    cd_hh_income_50k_to_59k: Optional[float] = Field(
        None,
        description="Household income from $50k to $59k in the congressional district",
    )
    cd_pct_hh_income_50k_to_59k: Optional[float] = Field(
        None,
        description="Percentage of household income from $50k to $59k in the congressional district",
    )
    cd_hh_income_60k_to_74k: Optional[float] = Field(
        None,
        description="Household income from $60k to $74k in the congressional district",
    )
    cd_pct_hh_income_60k_to_74k: Optional[float] = Field(
        None,
        description="Percentage of household income from $60k to $74k in the congressional district",
    )
    cd_hh_income_75k_to_99k: Optional[float] = Field(
        None,
        description="Household income from $75k to $99k in the congressional district",
    )
    cd_pct_hh_income_75k_to_99k: Optional[float] = Field(
        None,
        description="Percentage of household income from $75k to $99k in the congressional district",
    )
    cd_hh_income_100k_to_124k: Optional[float] = Field(
        None,
        description="Household income from $100k to $124k in the congressional district",
    )
    cd_pct_hh_income_100k_to_124k: Optional[float] = Field(
        None,
        description="Percentage of household income from $100k to $124k in the congressional district",
    )
    cd_hh_income_125k_to_149k: Optional[float] = Field(
        None,
        description="Household income from $125k to $149k in the congressional district",
    )
    cd_pct_hh_income_125k_to_149k: Optional[float] = Field(
        None,
        description="Percentage of household income from $125k to $149k in the congressional district",
    )
    cd_hh_income_150k_to_199k: Optional[float] = Field(
        None,
        description="Household income from $150k to $199k in the congressional district",
    )
    cd_pct_hh_income_150k_to_199k: Optional[float] = Field(
        None,
        description="Percentage of household income from $150k to $199k in the congressional district",
    )
    cd_hh_income_200k_or_more: Optional[float] = Field(
        None, description="Household income $200k or more in the congressional district"
    )
    cd_pct_hh_income_200k_or_more: Optional[float] = Field(
        None,
        description="Percentage of household income $200k or more in the congressional district",
    )
    cd_median_family_income: Optional[float] = Field(
        None, description="Median family income in the congressional district"
    )

    state_hh_income_total: Optional[float] = Field(
        None, description="Total household income in the state"
    )
    state_pct_hh_income_total: Optional[float] = Field(
        None, description="Percentage of total household income in the state"
    )
    state_hh_income_less_10k: Optional[float] = Field(
        None, description="Household income less than $10k in the state"
    )
    state_pct_hh_income_less_10k: Optional[float] = Field(
        None, description="Percentage of household income less than $10k in the state"
    )
    state_hh_income_10k_to_14k: Optional[float] = Field(
        None, description="Household income from $10k to $14k in the state"
    )
    state_pct_hh_income_10k_to_14k: Optional[float] = Field(
        None,
        description="Percentage of household income from $10k to $14k in the state",
    )
    state_hh_income_15k_to_19k: Optional[float] = Field(
        None, description="Household income from $15k to $19k in the state"
    )
    state_pct_hh_income_15k_to_19k: Optional[float] = Field(
        None,
        description="Percentage of household income from $15k to $19k in the state",
    )
    state_hh_income_20k_to_24k: Optional[float] = Field(
        None, description="Household income from $20k to $24k in the state"
    )
    state_pct_hh_income_20k_to_24k: Optional[float] = Field(
        None,
        description="Percentage of household income from $20k to $24k in the state",
    )
    state_hh_income_25k_to_29k: Optional[float] = Field(
        None, description="Household income from $25k to $29k in the state"
    )
    state_pct_hh_income_25k_to_29k: Optional[float] = Field(
        None,
        description="Percentage of household income from $25k to $29k in the state",
    )
    state_hh_income_30k_to_34k: Optional[float] = Field(
        None, description="Household income from $30k to $34k in the state"
    )
    state_pct_hh_income_30k_to_34k: Optional[float] = Field(
        None,
        description="Percentage of household income from $30k to $34k in the state",
    )
    state_hh_income_35k_to_39k: Optional[float] = Field(
        None, description="Household income from $35k to $39k in the state"
    )
    state_pct_hh_income_35k_to_39k: Optional[float] = Field(
        None,
        description="Percentage of household income from $35k to $39k in the state",
    )
    state_hh_income_40k_to_44k: Optional[float] = Field(
        None, description="Household income from $40k to $44k in the state"
    )
    state_pct_hh_income_40k_to_44k: Optional[float] = Field(
        None,
        description="Percentage of household income from $40k to $44k in the state",
    )
    state_hh_income_45k_to_49k: Optional[float] = Field(
        None, description="Household income from $45k to $49k in the state"
    )
    state_pct_hh_income_45k_to_49k: Optional[float] = Field(
        None,
        description="Percentage of household income from $45k to $49k in the state",
    )
    state_hh_income_50k_to_59k: Optional[float] = Field(
        None, description="Household income from $50k to $59k in the state"
    )
    state_pct_hh_income_50k_to_59k: Optional[float] = Field(
        None,
        description="Percentage of household income from $50k to $59k in the state",
    )
    state_hh_income_60k_to_74k: Optional[float] = Field(
        None, description="Household income from $60k to $74k in the state"
    )
    state_pct_hh_income_60k_to_74k: Optional[float] = Field(
        None,
        description="Percentage of household income from $60k to $74k in the state",
    )
    state_hh_income_75k_to_99k: Optional[float] = Field(
        None, description="Household income from $75k to $99k in the state"
    )
    state_pct_hh_income_75k_to_99k: Optional[float] = Field(
        None,
        description="Percentage of household income from $75k to $99k in the state",
    )
    state_hh_income_100k_to_124k: Optional[float] = Field(
        None, description="Household income from $100k to $124k in the state"
    )
    state_pct_hh_income_100k_to_124k: Optional[float] = Field(
        None,
        description="Percentage of household income from $100k to $124k in the state",
    )
    state_hh_income_125k_to_149k: Optional[float] = Field(
        None, description="Household income from $125k to $149k in the state"
    )
    state_pct_hh_income_125k_to_149k: Optional[float] = Field(
        None,
        description="Percentage of household income from $125k to $149k in the state",
    )
    state_hh_income_150k_to_199k: Optional[float] = Field(
        None, description="Household income from $150k to $199k in the state"
    )
    state_pct_hh_income_150k_to_199k: Optional[float] = Field(
        None,
        description="Percentage of household income from $150k to $199k in the state",
    )
    state_hh_income_200k_or_more: Optional[float] = Field(
        None, description="Household income $200k or more in the state"
    )
    state_pct_hh_income_200k_or_more: Optional[float] = Field(
        None, description="Percentage of household income $200k or more in the state"
    )
    state_median_family_income: Optional[float] = Field(
        None, description="Median family income in the state"
    )

    us_hh_income_total: Optional[float] = Field(
        None, description="Total household income in the US"
    )
    us_pct_hh_income_total: Optional[float] = Field(
        None, description="Percentage of total household income in the US"
    )
    us_hh_income_less_10k: Optional[float] = Field(
        None, description="Household income less than $10k in the US"
    )
    us_pct_hh_income_less_10k: Optional[float] = Field(
        None, description="Percentage of household income less than $10k in the US"
    )
    us_hh_income_10k_to_14k: Optional[float] = Field(
        None, description="Household income from $10k to $14k in the US"
    )
    us_pct_hh_income_10k_to_14k: Optional[float] = Field(
        None, description="Percentage of household income from $10k to $14k in the US"
    )
    us_hh_income_15k_to_19k: Optional[float] = Field(
        None, description="Household income from $15k to $19k in the US"
    )
    us_pct_hh_income_15k_to_19k: Optional[float] = Field(
        None, description="Percentage of household income from $15k to $19k in the US"
    )
    us_hh_income_20k_to_24k: Optional[float] = Field(
        None, description="Household income from $20k to $24k in the US"
    )
    us_pct_hh_income_20k_to_24k: Optional[float] = Field(
        None, description="Percentage of household income from $20k to $24k in the US"
    )
    us_hh_income_25k_to_29k: Optional[float] = Field(
        None, description="Household income from $25k to $29k in the US"
    )
    us_pct_hh_income_25k_to_29k: Optional[float] = Field(
        None, description="Percentage of household income from $25k to $29k in the US"
    )
    us_hh_income_30k_to_34k: Optional[float] = Field(
        None, description="Household income from $30k to $34k in the US"
    )
    us_pct_hh_income_30k_to_34k: Optional[float] = Field(
        None, description="Percentage of household income from $30k to $34k in the US"
    )
    us_hh_income_35k_to_39k: Optional[float] = Field(
        None, description="Household income from $35k to $39k in the US"
    )
    us_pct_hh_income_35k_to_39k: Optional[float] = Field(
        None, description="Percentage of household income from $35k to $39k in the US"
    )
    us_hh_income_40k_to_44k: Optional[float] = Field(
        None, description="Household income from $40k to $44k in the US"
    )
    us_pct_hh_income_40k_to_44k: Optional[float] = Field(
        None, description="Percentage of household income from $40k to $44k in the US"
    )
    us_hh_income_45k_to_49k: Optional[float] = Field(
        None, description="Household income from $45k to $49k in the US"
    )
    us_pct_hh_income_45k_to_49k: Optional[float] = Field(
        None, description="Percentage of household income from $45k to $49k in the US"
    )
    us_hh_income_50k_to_59k: Optional[float] = Field(
        None, description="Household income from $50k to $59k in the US"
    )
    us_pct_hh_income_50k_to_59k: Optional[float] = Field(
        None, description="Percentage of household income from $50k to $59k in the US"
    )
    us_hh_income_60k_to_74k: Optional[float] = Field(
        None, description="Household income from $60k to $74k in the US"
    )
    us_pct_hh_income_60k_to_74k: Optional[float] = Field(
        None, description="Percentage of household income from $60k to $74k in the US"
    )
    us_hh_income_75k_to_99k: Optional[float] = Field(
        None, description="Household income from $75k to $99k in the US"
    )
    us_pct_hh_income_75k_to_99k: Optional[float] = Field(
        None, description="Percentage of household income from $75k to $99k in the US"
    )
    us_hh_income_100k_to_124k: Optional[float] = Field(
        None, description="Household income from $100k to $124k in the US"
    )
    us_pct_hh_income_100k_to_124k: Optional[float] = Field(
        None, description="Percentage of household income from $100k to $124k in the US"
    )
    us_hh_income_125k_to_149k: Optional[float] = Field(
        None, description="Household income from $125k to $149k in the US"
    )
    us_pct_hh_income_125k_to_149k: Optional[float] = Field(
        None, description="Percentage of household income from $125k to $149k in the US"
    )
    us_hh_income_150k_to_199k: Optional[float] = Field(
        None, description="Household income from $150k to $199k in the US"
    )
    us_pct_hh_income_150k_to_199k: Optional[float] = Field(
        None, description="Percentage of household income from $150k to $199k in the US"
    )
    us_hh_income_200k_or_more: Optional[float] = Field(
        None, description="Household income $200k or more in the US"
    )
    us_pct_hh_income_200k_or_more: Optional[float] = Field(
        None, description="Percentage of household income $200k or more in the US"
    )
    us_median_family_income: Optional[float] = Field(
        None, description="Median family income in the US"
    )

    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5StateIncomeSchema(BaseModel):
    id: str = Field(..., description="Unique identifier")
    year: int = Field(..., description="Year of the data")
    state_fip: str = Field(..., description="State FIPS code")
    congressional_district: str = Field(..., description="Congressional district")
    hh_income_total: Optional[int] = Field(None, description="Total household income")
    hh_income_total_moe: Optional[int] = Field(None, description="Margin of error for total household income")
    hh_income_less_10k: Optional[int] = Field(None, description="Household income less than 10k")
    hh_income_less_10k_moe: Optional[int] = Field(None, description="Margin of error for household income less than 10k")
    pct_hh_income_less_10k: Optional[float] = Field(None, description="Percentage of households with income less than 10k")
    hh_income_10k_to_14k: Optional[int] = Field(None, description="Household income between 10k and 14k")
    hh_income_10k_to_14k_moe: Optional[int] = Field(None, description="Margin of error for household income between 10k and 14k")
    pct_hh_income_10k_to_14k: Optional[float] = Field(None, description="Percentage of households with income between 10k and 14k")
    hh_income_15k_to_19k: Optional[int] = Field(None, description="Household income between 15k and 19k")
    hh_income_15k_to_19k_moe: Optional[int] = Field(None, description="Margin of error for household income between 15k and 19k")
    pct_hh_income_15k_to_19k: Optional[float] = Field(None, description="Percentage of households with income between 15k and 19k")
    hh_income_20k_to_24k: Optional[int] = Field(None, description="Household income between 20k and 24k")
    hh_income_20k_to_24k_moe: Optional[int] = Field(None, description="Margin of error for household income between 20k and 24k")
    pct_hh_income_20k_to_24k: Optional[float] = Field(None, description="Percentage of households with income between 20k and 24k")
    hh_income_25k_to_29k: Optional[int] = Field(None, description="Household income between 25k and 29k")
    hh_income_25k_to_29k_moe: Optional[int] = Field(None, description="Margin of error for household income between 25k and 29k")
    pct_hh_income_25k_to_29k: Optional[float] = Field(None, description="Percentage of households with income between 25k and 29k")
    hh_income_30k_to_34k: Optional[int] = Field(None, description="Household income between 30k and 34k")
    hh_income_30k_to_34k_moe: Optional[int] = Field(None, description="Margin of error for household income between 30k and 34k")
    pct_hh_income_30k_to_34k: Optional[float] = Field(None, description="Percentage of households with income between 30k and 34k")
    hh_income_35k_to_39k: Optional[int] = Field(None, description="Household income between 35k and 39k")
    hh_income_35k_to_39k_moe: Optional[int] = Field(None, description="Margin of error for household income between 35k and 39k")
    pct_hh_income_35k_to_39k: Optional[float] = Field(None, description="Percentage of households with income between 35k and 39k")
    hh_income_40k_to_44k: Optional[int] = Field(None, description="Household income between 40k and 44k")
    hh_income_40k_to_44k_moe: Optional[int] = Field(None, description="Margin of error for household income between 40k and 44k")
    pct_hh_income_40k_to_44k: Optional[float] = Field(None, description="Percentage of households with income between 40k and 44k")
    hh_income_45k_to_49k: Optional[int] = Field(None, description="Household income between 45k and 49k")
    hh_income_45k_to_49k_moe: Optional[int] = Field(None, description="Margin of error for household income between 45k and 49k")
    pct_hh_income_45k_to_49k: Optional[float] = Field(None, description="Percentage of households with income between 45k and 49k")
    hh_income_50k_to_59k: Optional[int] = Field(None, description="Household income between 50k and 59k")
    hh_income_50k_to_59k_moe: Optional[int] = Field(None, description="Margin of error for household income between 50k and 59k")
    pct_hh_income_50k_to_59k: Optional[float] = Field(None, description="Percentage of households with income between 50k and 59k")
    hh_income_60k_to_74k: Optional[int] = Field(None, description="Household income between 60k and 74k")
    hh_income_60k_to_74k_moe: Optional[int] = Field(None, description="Margin of error for household income between 60k and 74k")
    pct_hh_income_60k_to_74k: Optional[float] = Field(None, description="Percentage of households with income between 60k and 74k")
    hh_income_75k_to_99k: Optional[int] = Field(None, description="Household income between 75k and 99k")
    hh_income_75k_to_99k_moe: Optional[int] = Field(None, description="Margin of error for household income between 75k and 99k")
    pct_hh_income_75k_to_99k: Optional[float] = Field(None, description="Percentage of households with income between 75k and 99k")
    hh_income_100k_to_124k: Optional[int] = Field(None, description="Household income between 100k and 124k")
    hh_income_100k_to_124k_moe: Optional[int] = Field(None, description="Margin of error for household income between 100k and 124k")
    pct_hh_income_100k_to_124k: Optional[float] = Field(None, description="Percentage of households with income between 100k and 124k")
    hh_income_125k_to_149k: Optional[int] = Field(None, description="Household income between 125k and 149k")
    hh_income_125k_to_149k_moe: Optional[int] = Field(None, description="Margin of error for household income between 125k and 149k")
    pct_hh_income_125k_to_149k: Optional[float] = Field(None, description="Percentage of households with income between 125k and 149k")
    hh_income_150k_to_199k: Optional[int] = Field(None, description="Household income between 150k and 199k")
    hh_income_150k_to_199k_moe: Optional[int] = Field(None, description="Margin of error for household income between 150k and 199k")
    pct_hh_income_150k_to_199k: Optional[float] = Field(None, description="Percentage of households with income between 150k and 199k")
    hh_income_200k_or_more: Optional[int] = Field(None, description="Household income of 200k or more")
    hh_income_200k_or_more_moe: Optional[int] = Field(None, description="Margin of error for household income of 200k or more")
    pct_hh_income_200k_or_more: Optional[float] = Field(None, description="Percentage of households with income of 200k or more")
    family_income_total: Optional[int] = Field(None, description="Total family income")
    family_income_total_moe: Optional[int] = Field(None, description="Margin of error for total family income")
    median_family_income: Optional[int] = Field(None, description="Median family income")
    median_family_income_moe: Optional[int] = Field(None, description="Margin of error for median family income")
    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5StateDemographicsSchema(BaseModel):
    id: str = Field(..., description="Unique identifier")
    year: int = Field(..., description="Year of the data")
    state_fip: str = Field(..., description="State FIPS code")
    total_population: Optional[int] = Field(None, description="Total population")
    total_population_moe: Optional[int] = Field(None, description="Margin of error for total population")
    sex_total: Optional[int] = Field(None, description="Total population by sex")
    sex_total_moe: Optional[int] = Field(None, description="Margin of error for total population by sex")
    sex_male: Optional[int] = Field(None, description="Male population")
    sex_male_moe: Optional[int] = Field(None, description="Margin of error for male population")
    pct_sex_male: Optional[float] = Field(None, description="Percentage of male population")
    male_voting_age_population: Optional[int] = Field(None, description="Male voting-age population")
    pct_male_voting_age_population: Optional[float] = Field(None, description="Percentage of male voting-age population")
    sex_female: Optional[int] = Field(None, description="Female population")
    sex_female_moe: Optional[int] = Field(None, description="Margin of error for female population")
    pct_sex_female: Optional[float] = Field(None, description="Percentage of female population")
    female_voting_age_population: Optional[int] = Field(None, description="Female voting-age population")
    pct_female_voting_age_population: Optional[float] = Field(None, description="Percentage of female voting-age population")
    race_white_total: Optional[int] = Field(None, description="White race population")
    race_white_total_moe: Optional[int] = Field(None, description="Margin of error for white race population")
    pct_race_white: Optional[float] = Field(None, description="Percentage of white race population")
    race_black_total: Optional[int] = Field(None, description="Black race population")
    race_black_total_moe: Optional[int] = Field(None, description="Margin of error for black race population")
    pct_race_black: Optional[float] = Field(None, description="Percentage of black race population")
    race_asian_total: Optional[int] = Field(None, description="Asian race population")
    race_asian_total_moe: Optional[int] = Field(None, description="Margin of error for Asian race population")
    pct_race_asian: Optional[float] = Field(None, description="Percentage of Asian race population")
    race_pacific_islander_total: Optional[int] = Field(None, description="Pacific Islander race population")
    race_pacific_islander_total_moe: Optional[int] = Field(None, description="Margin of error for Pacific Islander race population")
    pct_race_pacific_islander: Optional[float] = Field(None, description="Percentage of Pacific Islander race population")
    race_other_total: Optional[int] = Field(None, description="Other race population")
    race_other_total_moe: Optional[int] = Field(None, description="Margin of error for other race population")
    pct_race_other: Optional[float] = Field(None, description="Percentage of other race population")
    race_two_or_more_total: Optional[int] = Field(None, description="Population of two or more races")
    race_two_or_more_total_moe: Optional[int] = Field(None, description="Margin of error for population of two or more races")
    pct_race_two_or_more: Optional[float] = Field(None, description="Percentage of population of two or more races")
    hispanic_total: Optional[int] = Field(None, description="Hispanic population")
    hispanic_total_moe: Optional[int] = Field(None, description="Margin of error for Hispanic population")
    pct_hispanic: Optional[float] = Field(None, description="Percentage of Hispanic population")
    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5StateEmploymentSchema(BaseModel):
    id: str = Field(..., description="Unique identifier")
    year: int = Field(..., description="Year of the data")
    state_fip: str = Field(..., description="State FIPS code")
    employment_status_total: Optional[int] = Field(None, description="Total employment status")
    employment_status_total_moe: Optional[int] = Field(None, description="Margin of error for total employment status")
    in_labor_force: Optional[int] = Field(None, description="Number of people in the labor force")
    in_labor_force_moe: Optional[int] = Field(None, description="Margin of error for in labor force")
    pct_in_labor_force: Optional[float] = Field(None, description="Percentage of people in the labor force")
    not_in_labor_force: Optional[int] = Field(None, description="Number of people not in the labor force")
    not_in_labor_force_moe: Optional[int] = Field(None, description="Margin of error for not in labor force")
    pct_not_in_labor_force: Optional[float] = Field(None, description="Percentage of people not in the labor force")
    civilian_labor_force: Optional[int] = Field(None, description="Number of people in the civilian labor force")
    civilian_labor_force_moe: Optional[int] = Field(None, description="Margin of error for civilian labor force")
    pct_civilian_labor_force: Optional[float] = Field(None, description="Percentage of people in the civilian labor force")
    civilian_employed: Optional[int] = Field(None, description="Number of civilians employed")
    civilian_employed_moe: Optional[int] = Field(None, description="Margin of error for civilians employed")
    pct_civilian_employed: Optional[float] = Field(None, description="Percentage of civilians employed")
    civilian_unemployed: Optional[int] = Field(None, description="Number of civilians unemployed")
    civilian_unemployed_moe: Optional[int] = Field(None, description="Margin of error for civilians unemployed")
    pct_civilian_unemployed: Optional[float] = Field(None, description="Percentage of civilians unemployed")
    armed_forces: Optional[int] = Field(None, description="Number of people in the armed forces")
    armed_forces_moe: Optional[int] = Field(None, description="Margin of error for armed forces")
    pct_armed_forces_employed: Optional[float] = Field(None, description="Percentage of people in the armed forces")
    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5CountryEmploymentSchema(BaseModel):
    id: str = Field(..., description="Unique identifier")
    year: int = Field(..., description="Year of the data")
    employment_status_total: Optional[int] = Field(None, description="Total employment status")
    employment_status_total_moe: Optional[int] = Field(None, description="Margin of error for total employment status")
    in_labor_force: Optional[int] = Field(None, description="Number of people in the labor force")
    in_labor_force_moe: Optional[int] = Field(None, description="Margin of error for in labor force")
    pct_in_labor_force: Optional[float] = Field(None, description="Percentage of people in the labor force")
    not_in_labor_force: Optional[int] = Field(None, description="Number of people not in the labor force")
    not_in_labor_force_moe: Optional[int] = Field(None, description="Margin of error for not in labor force")
    pct_not_in_labor_force: Optional[float] = Field(None, description="Percentage of people not in the labor force")
    civilian_labor_force: Optional[int] = Field(None, description="Number of people in the civilian labor force")
    civilian_labor_force_moe: Optional[int] = Field(None, description="Margin of error for civilian labor force")
    pct_civilian_labor_force: Optional[float] = Field(None, description="Percentage of people in the civilian labor force")
    civilian_employed: Optional[int] = Field(None, description="Number of civilians employed")
    civilian_employed_moe: Optional[int] = Field(None, description="Margin of error for civilians employed")
    pct_civilian_employed: Optional[float] = Field(None, description="Percentage of civilians employed")
    civilian_unemployed: Optional[int] = Field(None, description="Number of civilians unemployed")
    civilian_unemployed_moe: Optional[int] = Field(None, description="Margin of error for civilians unemployed")
    pct_civilian_unemployed: Optional[float] = Field(None, description="Percentage of civilians unemployed")
    armed_forces: Optional[int] = Field(None, description="Number of people in the armed forces")
    armed_forces_moe: Optional[int] = Field(None, description="Margin of error for armed forces")
    pct_armed_forces_employed: Optional[float] = Field(None, description="Percentage of people in the armed forces")
    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5CountryDemographicsSchema(BaseModel):
    id: str = Field(..., description="Unique identifier")
    year: int = Field(..., description="Year of the data")
    total_population: Optional[int] = Field(None, description="Total population")
    total_population_moe: Optional[int] = Field(None, description="Margin of error for total population")
    sex_total: Optional[int] = Field(None, description="Total population by sex")
    sex_total_moe: Optional[int] = Field(None, description="Margin of error for total population by sex")
    sex_male: Optional[int] = Field(None, description="Male population")
    sex_male_moe: Optional[int] = Field(None, description="Margin of error for male population")
    pct_sex_male: Optional[float] = Field(None, description="Percentage of male population")
    male_voting_age_population: Optional[int] = Field(None, description="Male voting-age population")
    pct_male_voting_age_population: Optional[float] = Field(None, description="Percentage of male voting-age population")
    sex_female: Optional[int] = Field(None, description="Female population")
    sex_female_moe: Optional[int] = Field(None, description="Margin of error for female population")
    pct_sex_female: Optional[float] = Field(None, description="Percentage of female population")
    female_voting_age_population: Optional[int] = Field(None, description="Female voting-age population")
    pct_female_voting_age_population: Optional[float] = Field(None, description="Percentage of female voting-age population")
    race_white_total: Optional[int] = Field(None, description="White race population")
    race_white_total_moe: Optional[int] = Field(None, description="Margin of error for white race population")
    pct_race_white: Optional[float] = Field(None, description="Percentage of white race population")
    race_black_total: Optional[int] = Field(None, description="Black race population")
    race_black_total_moe: Optional[int] = Field(None, description="Margin of error for black race population")
    pct_race_black: Optional[float] = Field(None, description="Percentage of black race population")
    race_asian_total: Optional[int] = Field(None, description="Asian race population")
    race_asian_total_moe: Optional[int] = Field(None, description="Margin of error for Asian race population")
    pct_race_asian: Optional[float] = Field(None, description="Percentage of Asian race population")
    race_pacific_islander_total: Optional[int] = Field(None, description="Pacific Islander race population")
    race_pacific_islander_total_moe: Optional[int] = Field(None, description="Margin of error for Pacific Islander race population")
    pct_race_pacific_islander: Optional[float] = Field(None, description="Percentage of Pacific Islander race population")
    race_other_total: Optional[int] = Field(None, description="Other race population")
    race_other_total_moe: Optional[int] = Field(None, description="Margin of error for other race population")
    pct_race_other: Optional[float] = Field(None, description="Percentage of other race population")
    race_two_or_more_total: Optional[int] = Field(None, description="Population of two or more races")
    race_two_or_more_total_moe: Optional[int] = Field(None, description="Margin of error for population of two or more races")
    pct_race_two_or_more: Optional[float] = Field(None, description="Percentage of population of two or more races")
    hispanic_total: Optional[int] = Field(None, description="Hispanic population")
    hispanic_total_moe: Optional[int] = Field(None, description="Margin of error for Hispanic population")
    pct_hispanic: Optional[float] = Field(None, description="Percentage of Hispanic population")
    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True

class ACS5CountryIncomeSchema(BaseModel):
    id: str = Field(..., description="Unique identifier")
    year: int = Field(..., description="Year of the data")
    state_fip: str = Field(..., description="State FIPS code")
    total_population: Optional[int] = Field(None, description="Total population")
    total_population_moe: Optional[int] = Field(None, description="Margin of error for total population")
    sex_total: Optional[int] = Field(None, description="Total population by sex")
    sex_total_moe: Optional[int] = Field(None, description="Margin of error for total population by sex")
    sex_male: Optional[int] = Field(None, description="Male population")
    sex_male_moe: Optional[int] = Field(None, description="Margin of error for male population")
    pct_sex_male: Optional[float] = Field(None, description="Percentage of male population")
    male_voting_age_population: Optional[int] = Field(None, description="Male voting-age population")
    pct_male_voting_age_population: Optional[float] = Field(None, description="Percentage of male voting-age population")
    sex_female: Optional[int] = Field(None, description="Female population")
    sex_female_moe: Optional[int] = Field(None, description="Margin of error for female population")
    pct_sex_female: Optional[float] = Field(None, description="Percentage of female population")
    female_voting_age_population: Optional[int] = Field(None, description="Female voting-age population")
    pct_female_voting_age_population: Optional[float] = Field(None, description="Percentage of female voting-age population")
    race_white_total: Optional[int] = Field(None, description="White race population")
    race_white_total_moe: Optional[int] = Field(None, description="Margin of error for white race population")
    pct_race_white: Optional[float] = Field(None, description="Percentage of white race population")
    race_black_total: Optional[int] = Field(None, description="Black race population")
    race_black_total_moe: Optional[int] = Field(None, description="Margin of error for black race population")
    pct_race_black: Optional[float] = Field(None, description="Percentage of black race population")
    race_asian_total: Optional[int] = Field(None, description="Asian race population")
    race_asian_total_moe: Optional[int] = Field(None, description="Margin of error for Asian race population")
    pct_race_asian: Optional[float] = Field(None, description="Percentage of Asian race population")
    race_pacific_islander_total: Optional[int] = Field(None, description="Pacific Islander race population")
    race_pacific_islander_total_moe: Optional[int] = Field(None, description="Margin of error for Pacific Islander race population")
    pct_race_pacific_islander: Optional[float] = Field(None, description="Percentage of Pacific Islander race population")
    race_other_total: Optional[int] = Field(None, description="Other race population")
    race_other_total_moe: Optional[int] = Field(None, description="Margin of error for other race population")
    pct_race_other: Optional[float] = Field(None, description="Percentage of other race population")
    race_two_or_more_total: Optional[int] = Field(None, description="Population of two or more races")
    race_two_or_more_total_moe: Optional[int] = Field(None, description="Margin of error for population of two or more races")
    pct_race_two_or_more: Optional[float] = Field(None, description="Percentage of population of two or more races")
    hispanic_total: Optional[int] = Field(None, description="Hispanic population")
    hispanic_total_moe: Optional[int] = Field(None, description="Margin of error for Hispanic population")
    pct_hispanic: Optional[float] = Field(None, description="Percentage of Hispanic population")
    class Config:
        from_attributes = True
        populate_by_name = True
        str_strip_whitespace = True
        use_enum_values = True
        validate_assignment = True
