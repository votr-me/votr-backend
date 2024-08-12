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
