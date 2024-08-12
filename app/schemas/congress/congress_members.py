from pydantic import BaseModel, Field, validator, field_serializer
from typing import Optional, List
from datetime import date, datetime


def convert_date_to_string(value: date) -> str:
    return value.isoformat()


class CongressMemberSchema(BaseModel):
    bioguide_id: str = Field(...)
    is_current_member: bool = Field(...)
    birthday: Optional[date] = Field(
        ...,
    )
    member_age: Optional[float] = Field(None)
    last_name: str = Field(...)
    first_name: str = Field(...)
    middle_name: Optional[str] = Field(None)
    suffix: Optional[str] = Field(None)
    member_party: str = Field(...)
    member_state: str = Field(...)
    member_district: Optional[str] = Field(None)  # Handle float or missing
    member_type: str = Field(...)
    member_title: str = Field(...)
    depiction_image_url: Optional[str] = Field(None)
    depiction_attribution: Optional[str] = Field(None)
    leadership_titles: Optional[List[str]] = Field(None)
    address: Optional[str] = Field(None)
    office_phone_number: Optional[str] = Field(None)
    contact_form: Optional[str] = Field(None)
    office_address: Optional[str] = Field(None)
    office_city: Optional[str] = Field(None)
    office_zipcode: Optional[int] = Field(None)
    official_website_url: Optional[str] = Field(None)
    thomas_id: Optional[str] = Field(None)
    opensecrets_id: Optional[str] = Field(None)
    lis_id: Optional[str] = Field(None)
    govtrack_id: Optional[str] = Field(None)
    votesmart_id: Optional[str] = Field(None)
    ballotpedia_id: Optional[str] = Field(None)
    icpsr_id: Optional[str] = Field(None)
    wikipedia_id: Optional[str] = Field(None)
    fec_ids: Optional[List[str]] = Field(None)

    class Config:
        from_attributes = True
        populate_by_name = (True,)
        populate_by_name = True

    @field_serializer("birthday")  # Serialize the aliased field
    def serialize_birthday(cls, v: str) -> str:
        try:
            # Attempt to parse the string if it's not already a date
            date_obj = date.fromisoformat(v)
            return date_obj.isoformat()
        except (ValueError, TypeError):
            # Handle invalid date formats gracefully
            return None


class CongressMemberSponsoredBillsSchema(BaseModel):
    bioguide_id: str = Field(...)
    policy_area_name: Optional[str] = Field(None)
    sponsorship_type: str = Field(...)
    congress: int = Field(...)
    num_total_bills: int = Field(...)
    num_bills_by_policy_area: Optional[int] = Field(...)
    pct_of_total_bills: Optional[float] = Field(...)

    class Config:
        from_attributes = True
        populate_by_name = True


class CongressMemberTermsSchema(BaseModel):
    bioguide_id: str = Field(...)
    is_current_member: bool = Field(...)
    chamber: str = Field(...)
    member_type: str = Field(...)
    congress: str = Field(...)
    state_code: str = Field(...)
    state_name: str = Field(...)
    district: Optional[str] = Field(None)  # Districts can be None for Senators
    start_year: int = Field(...)
    end_year: Optional[int] = Field(None)

    class Config:
        from_attributes = True
        populate_by_name = True
