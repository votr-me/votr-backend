from datetime import date
from typing import Optional, List

from pydantic import BaseModel, field_validator


class CongressMemberBase(BaseModel):
    bioguide_id: str
    is_current_member: Optional[bool] = None
    birthday: Optional[str] = None
    member_age: Optional[int] = None
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    suffix: Optional[str] = None
    member_party: str
    member_state: str
    member_district: Optional[int] = None
    member_type: str
    member_title: str
    depiction_image_url: Optional[str] = None
    depiction_attribution: Optional[str] = None
    address: Optional[str] = None
    office_phone_number: Optional[str] = None
    contact_form: Optional[str] = None
    office_address: Optional[str] = None
    office_city: Optional[str] = None
    office_zipcode: Optional[int] = None
    official_website_url: Optional[str] = None
    thomas_id: Optional[str] = None
    opensecrets_id: Optional[str] = None
    lis_id: Optional[str] = None
    govtrack_id: Optional[str] = None
    votesmart_id: Optional[str] = None
    ballotpedia_id: Optional[str] = None
    icpsr_id: Optional[str] = None
    wikipedia_id: Optional[str] = None
    fec_ids: Optional[List[str]] = None


class CongressMemberCreate(CongressMemberBase):
    pass


class CongressMemberUpdate(CongressMemberBase):
    pass


class CongressMemberOut(BaseModel):
    bioguide_id: str
    is_current_member: Optional[bool] = None
    birthday: Optional[str] = None
    member_age: Optional[int] = None
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    suffix: Optional[str] = None
    member_party: str
    member_state: str
    member_district: Optional[int] = None
    member_type: str
    member_title: str
    depiction_image_url: Optional[str] = None
    depiction_attribution: Optional[str] = None
    address: Optional[str] = None
    office_phone_number: Optional[str] = None
    contact_form: Optional[str] = None
    office_address: Optional[str] = None
    office_city: Optional[str] = None
    office_zipcode: Optional[int] = None
    official_website_url: Optional[str] = None
    thomas_id: Optional[str] = None
    opensecrets_id: Optional[str] = None
    lis_id: Optional[str] = None
    govtrack_id: Optional[str] = None
    votesmart_id: Optional[str] = None
    ballotpedia_id: Optional[str] = None
    icpsr_id: Optional[str] = None
    wikipedia_id: Optional[str] = None
    fec_ids: Optional[List[str]] = None

    @field_validator('birthday', check_fields=True)
    def serialize_birthday(cls, v):
        if isinstance(v, date):
            return v.isoformat()
        return v

    class Config:
        from_attributes = True
