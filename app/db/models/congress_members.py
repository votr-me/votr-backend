from sqlalchemy import Column, Integer, String, Boolean, Date, Text, ARRAY

from .base_model import BaseModel


class CongressMember(BaseModel):
    __tablename__ = 'congress_members'

    bioguide_id = Column(String, primary_key=True, index=True)
    is_current_member = Column(Boolean, nullable=True)
    birthday = Column(Date, nullable=True)
    member_age = Column(Integer, nullable=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    suffix = Column(String, nullable=True)
    member_party = Column(String, nullable=False)
    member_state = Column(String, nullable=False)
    member_district = Column(Integer, nullable=True)
    member_type = Column(String, nullable=False)
    member_title = Column(String, nullable=False)
    depiction_image_url = Column(Text, nullable=True)
    depiction_attribution = Column(Text, nullable=True)
    address = Column(Text, nullable=True)
    office_phone_number = Column(String, nullable=True)
    contact_form = Column(Text, nullable=True)
    office_address = Column(Text, nullable=True)
    office_city = Column(String, nullable=True)
    office_zipcode = Column(Integer, nullable=True)
    official_website_url = Column(Text, nullable=True)
    thomas_id = Column(String, nullable=True)
    opensecrets_id = Column(String, nullable=True)
    lis_id = Column(String, nullable=True)
    govtrack_id = Column(String, nullable=True)
    votesmart_id = Column(String, nullable=True)
    ballotpedia_id = Column(String, nullable=True)
    icpsr_id = Column(String, nullable=True)
    wikipedia_id = Column(String, nullable=True)
    fec_ids = Column(ARRAY(String), nullable=True)
