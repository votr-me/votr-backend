import strawberry
from app.graphql.resolvers.congress_member_resolver import Query as CongressMemberQuery
from app.graphql.resolvers.acs5_resolver import Query as ACS5Query


# Combine the query classes using multiple inheritance
@strawberry.type
class Query(ACS5Query, CongressMemberQuery):
    pass


schema = strawberry.Schema(query=Query)
