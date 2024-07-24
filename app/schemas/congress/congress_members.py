from datetime import date
from typing import Optional, List

from pydantic import BaseModel, field_validator, Field


class CongressMemberBase(BaseModel):
    bioguide_id: str = Field(..., description="Bioguide ID of the congress member", example="A000376")
    member_age: int = Field(..., description="Current age of Member", example='50'),
    is_current_member: bool = Field(default=True, description="Indicates if the member is currently serving")
    birthday: date = Field(..., description="Congress member's birthday")
    member_age: Optional[int] = Field(None, description="Age of the congress member (derived from birthday)", ge=25, le=120)  # Assuming min/max ages
    last_name: str = Field(..., description="Last name of the congress member", example="Smith")
    first_name: str = Field(..., description="First name of the congress member", example="John")
    middle_name: Optional[str] = Field(None, description="Middle name of the congress member")
    suffix: Optional[str] = Field(None, description="Suffix of the congress member (e.g., Jr., Sr.)")
    member_party: str = Field(..., description="Political party affiliation (e.g., Democrat, Republican)", example="Republican")
    member_state: str = Field(..., description="State represented by the congress member", example="CA")
    member_district: Optional[int] = Field(None, description="District represented (if applicable)", ge=1)
    member_type: str = Field(..., description="Type of member (e.g., Rep, Sen)", example="Rep")
    member_title: str = Field(..., description="Formal title (e.g., Representative, Senator)", example="Representative")
    depiction_image_url: Optional[str] = Field(None, description="URL of the congress member's image")
    depiction_attribution: Optional[str] = Field(None, description="Attribution for the image (if applicable)")
    address: Optional[str] = Field(None, description="Congress member's address")
    office_phone_number: Optional[str] = Field(None, description="Congress member's office phone number")
    contact_form: Optional[str] = Field(None, description="URL of the congress member's contact form")
    office_address: Optional[str] = Field(None, description="Address of the congress member's office")
    office_city: Optional[str] = Field(None, description="City of the congress member's office")
    office_zipcode: Optional[int] = Field(None, description="ZIP code of the congress member's office")
    official_website_url: Optional[str] = Field(None, description="URL of the congress member's official website")
    thomas_id: Optional[str] = Field(None, description="Thomas ID of the congress member")
    opensecrets_id: Optional[str] = Field(None, description="OpenSecrets ID of the congress member")
    lis_id: Optional[str] = Field(None, description="LIS ID of the congress member")
    govtrack_id: Optional[str] = Field(None, description="GovTrack ID of the congress member")
    votesmart_id: Optional[str] = Field(None, description="VoteSmart ID of the congress member")
    ballotpedia_id: Optional[str] = Field(None, description="Ballotpedia ID of the congress member")
    icpsr_id: Optional[str] = Field(None, description="ICPSR ID of the congress member")
    wikipedia_id: Optional[str] = Field(None, description="Wikipedia ID of the congress member")
    fec_ids: Optional[List[str]] = Field(None, description="List of FEC IDs of the congress member")

class CongressMemberOut(CongressMemberBase):
    pass

    class Config:
        from_attributes = True
