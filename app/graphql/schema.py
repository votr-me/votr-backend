import strawberry
from app.graphql.resolvers.congress_member_resolver import Query

schema = strawberry.Schema(query=Query)
