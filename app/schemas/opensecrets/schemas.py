from pydantic import BaseModel, Field, HttpUrl, validator
from enum import Enum
from typing import Optional
from datetime import date, datetime
from pydantic_extra_types.phone_numbers import PhoneNumber
import re
import phonenumbers


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"


class Party(str, Enum):
    DEMOCRAT = "D"
    REPUBLICAN = "R"
    INDEPENDENT = "I"
    THIRD_PARTY = "3"
    LIBERTARIAN = "L"
    UKNOWN = "Unknown"


class Legislator(BaseModel):
    cid: str = Field(..., description="CRP ID for legislator")
    firstlast: str = Field(..., description="Full name like 'Nancy Pelosi'")
    lastname: str = Field(..., description="Last name of legislator")
    party: Optional[Party] = Field(None, description="Party affiliation")
    office: Optional[str] = Field(None, description="Office identifier")
    gender: Gender = Field(..., description="M or F")
    first_elected: int = Field(..., description="Year first elected to current office")
    exit_code: str = Field(..., description="Exit code assigned by CRP")
    comments: Optional[str] = Field(None, description="Explanation of exit code")
    phone: Optional[PhoneNumber] = Field(None, description="Office phone number")
    fax: Optional[PhoneNumber] = Field(None, description="Office fax number")
    website: Optional[HttpUrl] = Field(None, description="Legislator's website")
    webform: Optional[str] = Field(
        None, description="Form to communicate with legislator"
    )
    congress_office: Optional[str] = Field(None, description="Office address")
    bioguide_id: Optional[str] = Field(None, description="Bioguide ID of member")
    votesmart_id: Optional[str] = Field(None, description="VoteSmart ID of member")
    feccandid: Optional[str] = Field(
        None, description="ID assigned by Federal Election Commission"
    )
    twitter_id: Optional[str] = Field(None, description="Twitter ID of member")
    youtube_url: Optional[str] = Field(None, description="YouTube URL of member")
    facebook_id: Optional[str] = Field(None, description="Facebook ID of member")
    birthdate: Optional[date] = Field(
        None, description="Member's date of birth (YYYY-MM-DD)"
    )

    @validator("gender")
    def gender_must_be_valid(cls, value):
        if value not in Gender.__members__.values():
            raise ValueError("Gender must be either 'M' or 'F'")
        return value

    @validator("birthdate", pre=True, always=True)
    def birthdate_must_be_valid(cls, value):
        if value in [None, ""]:
            return None
        try:
            return datetime.strptime(str(value), "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Birthdate must be in the format YYYY-MM-DD")

    @validator("first_elected")
    def first_elected_must_be_valid_year(cls, value):
        if not (1789 <= value <= date.today().year):  # US Congress started in 1789
            raise ValueError(f"Invalid election year: {value}")
        return value

    @validator("phone", pre=True)
    def validate_phone_number(cls, value):
        if not value:
            return None  # Allow empty phone
        try:
            if value.startswith("tel:"):
                value = value[4:]  # Remove 'tel:'
            parsed_number = phonenumbers.parse(value, "US")
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError(f"Invalid phone number: {value}")
            # Store in E.164 format for consistency:
            return phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )
        except phonenumbers.NumberParseException:
            raise ValueError(f"Invalid phone number format: {value}")

    @validator("fax", pre=True)
    def validate_fax_number(cls, value):
        if not value:
            return None  # Allow empty fax
        try:
            if value.startswith("tel:"):
                value = value[4:]  # Remove 'tel:'
            parsed_number = phonenumbers.parse(value, "US")
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError(f"Invalid fax number: {value}")
            # Store in E.164 format for consistency:
            return phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )
        except phonenumbers.NumberParseException:
            raise ValueError(f"Invalid fax number format: {value}")

    @validator("website")
    def website_must_be_valid(cls, value):
        if value in [None, ""]:
            return None
        pattern = r"^(https?://)?([\w\-]+\.)+[\w\-]+(/[\w\- ./?%&=]*)?$"
        if not re.match(pattern, str(value)):
            raise ValueError(f"Invalid website URL: {value}")
        return value
