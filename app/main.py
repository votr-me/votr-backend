from contextlib import asynccontextmanager
from uuid import uuid4

from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.exceptions import HTTPException

from app.api.routes import api_router
from app.core.config import config
from app.core.redis import RedisPool
from app.services import LegislatorService
from app.dependencies import get_legislator_service
from app.data import init_db, close_db

# from app.graphql.schema import schema
import logging

# Configure logging
logger = logging.getLogger(__name__)
redis_pool = RedisPool(config.REDIS_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event to initialize and shut down resources (Redis, DB)"""
    try:
        await redis_pool.start()
        redis_client = await redis_pool.get_pool()
        FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
        app.state.redis_pool = redis_pool  # Store pool in app state for future use
        await init_db()
        logger.info("Application startup successful")
        yield  # Proceed to serve the application
    except Exception as e:
        logger.error(f"Error during application startup: {e}")
        raise
    finally:
        await redis_pool.stop()
        await close_db()
        logger.info("Application shutdown successful")


# async def get_context(
#     db: AsyncSession = Depends(get_session),
#     redis: RedisPool = Depends(get_redis_pool),
# ):
#     """Dependency injection for GraphQL context"""
#     return {"db": db, "redis": redis}


# Initialize FastAPI app with a lifespan context manager
app = FastAPI(
    name=config.APP_NAME,
    description=config.PROJECT_DESCRIPTION,
    version=config.PROJECT_VERSION,
    lifespan=lifespan,
)

# GraphQL router with context
# graphql_app = GraphQLRouter(schema, context_getter=get_context)

# Add middleware for correlation IDs and CORS
app.add_middleware(
    CorrelationIdMiddleware,
    header_name="X-Request-ID",
    update_request_header=True,
    generator=lambda: uuid4().hex,
    validator=is_valid_uuid4,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(api_router, prefix="/api/v1")
# app.include_router(graphql_app, prefix="/graphql")
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
