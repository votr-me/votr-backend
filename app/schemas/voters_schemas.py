from pydantic import BaseModel, Field
from typing import Optional


class VoterInfo(BaseModel):
    state: str = Field(..., description="Address State")
    state_fips: str = Field(..., description="FIPS code for state")
    bioguide_ids: list[str] = Field(
        ..., description="list of bioguide_ids for address Legislators"
    )
    district_number: str = Field(
        ..., description="the congressional district number for address"
    )
    district_name: Optional[str] = Field(
        None, description="Formal name for congressional district"
    )
    address: str = Field(..., description="address provided")

    class Config:
        from_attributes = True
        populate_by_name = True
