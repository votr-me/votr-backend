from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ARRAY, ForeignKey, Float
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy.orm import relationship

from .base_model import BaseModel


class CongressMember(BaseModel):
    __tablename__ = 'congress_members_historical'
    
    bioguide_id = Column(String, primary_key=True, index=True)
    is_current_member = Column(Boolean)
    birthday = Column(Date)
    member_age = Column(Float)
    last_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    suffix = Column(String)
    member_party = Column(String)
    member_state = Column(String)
    member_district = Column(Float)
    member_type = Column(String)
    member_title = Column(String)
    depiction_image_url = Column(String)
    depiction_attribution = Column(String)
    leadership_titles = Column(JSON)
    address = Column(String)
    office_phone_number = Column(String)
    contact_form = Column(String)
    office_address = Column(String)
    office_city = Column(String)
    office_zipcode = Column(Integer)
    official_website_url = Column(String)
    thomas_id = Column(String)
    opensecrets_id = Column(String)
    lis_id = Column(String)
    govtrack_id = Column(String)
    votesmart_id = Column(String)
    ballotpedia_id = Column(String)
    icpsr_id = Column(String)
    wikipedia_id = Column(String)
    fec_ids = Column(ARRAY(String))    


class CongressMemberSponsoredBills(BaseModel):
    __tablename__ = 'member_legislation_activity_cong_policy_area_historical'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    bioguide_id = Column(String)
    congress = Column(Integer)
    policy_area_name = Column(String)
    num_bills_sponsored = Column(String)
    num_bills_cosponsored = Column(Integer)

class CongressMemberTerms(BaseModel):
    __tablename__ = 'dim_congress_member_terms_historical'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    bioguide_id = Column(String)
    is_current_member = Column(Boolean)
    chamber = Column(String)
    member_type = Column(String)
    congress = Column(String)
    state_code = Column(String)
    state_name = Column(String)
    district = Column(String)
    start_year = Column(Integer)
    end_year = Column(Integer)
