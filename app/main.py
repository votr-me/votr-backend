from contextlib import asynccontextmanager
from uuid import uuid4
from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from app.api.routes import api_router
from app.core.config import config
from app.core.redis import RedisPool
from app.data import init_db, close_db
from strawberry.fastapi import GraphQLRouter
from app.dependencies import get_context

from app.graphql.schema import schema
import logging

# Configure logging
logger = logging.getLogger(__name__)
redis_pool = RedisPool(config.REDIS_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event to initialize and shut down resources (Redis, DB)."""
    try:
        # Initialize Redis pool
        await redis_pool.start()
        redis_client = await redis_pool.get_pool()
        FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

        # Store Redis pool in app state for access in other parts of the app
        app.state.redis_pool = redis_pool

        # Initialize the database (e.g., create tables)
        await init_db()

        logger.info("Application startup successful")
        yield  # Proceed to serve the application
    except Exception as e:
        logger.exception("Error during application startup")
        raise e
    finally:
        # Close Redis pool and database connections
        await redis_pool.stop()
        await close_db()
        logger.info("Application shutdown successful")


app = FastAPI(
    name=config.APP_NAME,
    description=config.PROJECT_DESCRIPTION,
    version=config.PROJECT_VERSION,
    lifespan=lifespan,
)

graphql_app = GraphQLRouter(schema, context_getter=get_context)

app.add_middleware(
    CorrelationIdMiddleware,
    header_name="X-Request-ID",
    update_request_header=True,
    generator=lambda: uuid4().hex,
    validator=is_valid_uuid4,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
