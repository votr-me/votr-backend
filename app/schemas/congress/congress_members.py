from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional, Union

def convert_date_to_string(dt: date) -> str:
    return dt.isoformat()

class CongressMemberSchema(BaseModel):
    bioguideId: str = Field(..., alias="bioguide_id")  
    isCurrentMember: bool = Field(..., alias="is_current_member")
    birthday: date = Field(..., json_encoders={date: convert_date_to_string}),
    memberAge: Optional[float] = Field(None, alias="member_age")
    lastName: str = Field(..., alias="last_name")
    firstName: str = Field(..., alias="first_name")
    middleName: Optional[str] = Field(None, alias="middle_name")
    suffix: Optional[str]
    memberParty: str = Field(..., alias="member_party")
    memberState: str = Field(..., alias="member_state")
    memberDistrict: Optional[Union[int, float]] = Field(None, alias="member_district")  # Handle float or missing
    memberType: str = Field(..., alias="member_type")
    memberTitle: str = Field(..., alias="member_title")
    depictionImageUrl: Optional[str] = Field(None, alias="depiction_image_url")
    depictionAttribution: Optional[str] = Field(None, alias="depiction_attribution")
    leadershipTitles: Optional[List[str]] = Field(None, alias="leadership_titles")
    address: Optional[str]
    officePhoneNumber: Optional[str] = Field(None, alias="office_phone_number")
    contactForm: Optional[str] = Field(None, alias="contact_form")
    officeAddress: Optional[str] = Field(None, alias="office_address")
    officeCity: Optional[str] = Field(None, alias="office_city")
    officeZipcode: Optional[int] = Field(None, alias="office_zipcode")
    officialWebsiteUrl: Optional[str] = Field(None, alias="official_website_url")
    thomasId: Optional[str] = Field(None, alias="thomas_id")
    opensecretsId: Optional[str] = Field(None, alias="opensecrets_id")
    lisId: Optional[str] = Field(None, alias="lis_id")
    govtrackId: Optional[str] = Field(None, alias="govtrack_id")
    votesmartId: Optional[str] = Field(None, alias="votesmart_id")
    ballotpediaId: Optional[str] = Field(None, alias="ballotpedia_id")
    icpsrId: Optional[str] = Field(None, alias="icpsr_id")
    wikipediaId: Optional[str] = Field(None, alias="wikipedia_id")
    fecIds: Optional[List[str]] = Field(None, alias="fec_ids")

    class Config:
        populate_by_name = True  
        from_attributes = True   

class CongressMemberSponsoredBillsSchema(BaseModel):
    bioguideId: str = Field(..., alias="bioguide_id")
    congress: int = Field(..., alias="congress")
    policy_area_name: str = Field(..., alias="policy_area_name")
    numBillsSponsored: int = Field(..., alias="num_bills_sponsored")
    numBillsCosponsored: int = Field(..., alias="num_bills_cosponsored")
    class Config:
        populate_by_name = True
        from_attributes = True


class CongressMemberTermsSchema(BaseModel):
    bioguideId: str = Field(..., alias="bioguide_id")
    isCurrentMember: bool = Field(..., alias="is_current_member")
    chamber: str
    memberType: str = Field(..., alias="member_type")
    congress: str  
    stateCode: str = Field(..., alias="state_code")
    stateName: str = Field(..., alias="state_name")
    district: Optional[str]  # Districts can be None for Senators
    startYear: int = Field(..., alias="start_year")
    endYear: int = Field(..., alias="end_year")

    class Config:
        populate_by_name = True
        from_attributes = True