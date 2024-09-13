from sqlalchemy import Column, Integer, String, Boolean, Date, ARRAY, Float
# from sqlalchemy.dialects.postgresql import ARRAY

from .base import BaseModel


class Legislator(BaseModel):
    __tablename__ = "legislators"

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
    member_district = Column(String)
    member_type = Column(String)
    member_title = Column(String)
    depiction_image_url = Column(String)
    depiction_attribution = Column(String)
    leadership_type = Column(String)
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


class LegislatorSponsoredBills(BaseModel):
    __tablename__ = "legislator_sponsor_congress_policy_area_historical"

    id = Column(String, primary_key=True)
    bioguide_id = Column(String)
    policy_area_name = Column(String)
    sponsorship_type = Column(String)
    congress = Column(Integer)
    num_total_bills = Column(Integer)
    num_bills_by_policy_area = Column(Integer)
    pct_of_total_bills = Column(Float)


class LegislatorTerms(BaseModel):
    __tablename__ = "dim_legislator_terms_historical"

    id = Column(Integer, primary_key=True)
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
