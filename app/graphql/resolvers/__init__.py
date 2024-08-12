from app.graphql.resolvers.congress_member_resolver import Query as congress_member_resolver_query
import strawberry
def combine_queries(*queries):
    @strawberry.type
    class Query(*queries):
        pass
    
    return Query
    
Query = combine_queries(
    congress_member_resolver_query
    )

__all__ = [
    congress_member_resolver_query
]