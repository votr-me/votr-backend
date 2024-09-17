import strawberry
from app.graphql.resolvers.legislator_resolver import Query as LegislatorQuery


@strawberry.type
class Query(LegislatorQuery):
    pass


schema = strawberry.Schema(query=Query)
