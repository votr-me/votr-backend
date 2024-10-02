from app.schemas import (
    LegislatorSchema,
    LegislatorTermsSchema,
    LegislatorSponsoredBillsSchema,
)
import strawberry
from typing import List, Optional
from datetime import date


@strawberry.type
class LegislatorLeadership:
    congress: str
    role: str

@strawberry.type
class Legislator:
    bioguide_id: str
    is_current_member: bool
    birthday: Optional[date]
    member_age: Optional[float]
    last_name: str
    first_name: str
    middle_name: Optional[str]
    suffix: Optional[str]
    member_party: str
    member_state: str
    member_district: Optional[str]
    member_type: str
    member_title: str
    depiction_image_url: Optional[str]
    depiction_attribution: Optional[str]
    address: Optional[str]
    office_phone_number: Optional[str]
    contact_form: Optional[str]
    office_address: Optional[str]
    office_city: Optional[str]
    office_zipcode: Optional[int]
    official_website_url: Optional[str]
    thomas_id: Optional[str]
    opensecrets_id: Optional[str]
    lis_id: Optional[str]
    govtrack_id: Optional[str]
    votesmart_id: Optional[str]
    ballotpedia_id: Optional[str]
    icpsr_id: Optional[str]
    wikipedia_id: Optional[str]
    fec_ids: Optional[List[str]]
    num_sponsored_legislation: Optional[int]
    num_cosponsored_legislation: Optional[int]
    term_count: Optional[int]
    first_year_in_chamber: Optional[int]
    last_year_in_chamber: Optional[int]
    total_years_served: Optional[int]
    num_congresses_served: Optional[int]


@strawberry.experimental.pydantic.type(model=LegislatorTermsSchema, all_fields=True)
class LegislatorTerms:
    pass


@strawberry.experimental.pydantic.type(
    model=LegislatorSponsoredBillsSchema, all_fields=True
)
class LegislatorSponsoredBills:
    pass


@strawberry.type
class LegislatorDetails:
    legislator: Legislator
    terms: List[LegislatorTerms]
    sponsored_bills: List[LegislatorSponsoredBills]
    leadership: Optional[List[LegislatorLeadership]]
