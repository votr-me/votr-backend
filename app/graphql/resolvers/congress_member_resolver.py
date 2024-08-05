import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def helloWorld(self) -> str:
        return "Hello, world!"

    # async def congress_member_with_details(
    #     self,
    #     bioguide_id: str,
    #     db: AsyncSession = Depends(get_db)
    # ) -> CongressMemberDetails:
    #     db_congress_member = await get_by_bioguide_id(db, bioguide_id=bioguide_id)
    #     if db_congress_member is None:
    #         raise HTTPException(status_code=404, detail="CongressMember not found")

    #     db_terms = await get_terms_by_bioguide_id(db, bioguide_id=bioguide_id)
    #     db_sponsored_bills = await get_sponsored_bills_by_bioguide_id(db, bioguide_id=bioguide_id)
    #     db_demographics = await get_acs5_demographics(db, member_district=db_congress_member.member_district, member_state=db_congress_member.member_state)
    #     db_employment = await get_acs5_employment(db, member_district=db_congress_member.member_district, member_state=db_congress_member.member_state)
    #     db_income = await get_acs5_income(db, member_district=db_congress_member.member_district, member_state=db_congress_member.member_state)

    #     return CongressMemberDetails(
    #         congress_member=CongressMember.from_pydantic(db_congress_member),
    #         terms=[CongressMemberTerms.from_pydantic(term) for term in db_terms],
    #         sponsored_bills=[CongressMemberSponsoredBills.from_pydantic(bill) for bill in db_sponsored_bills],
    #         demographics=ACS5Demographics.from_pydantic(db_demographics),
    #         employment=ACS5Employment.from_pydantic(db_employment),
    #         income=ACS5Income.from_pydantic(db_income)
    #     )
