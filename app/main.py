import logging
from contextlib import asynccontextmanager
from uuid import uuid4

from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import config
from app.core.logging_config import configure_logging
from app.core.redis import redis_pool
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from app.db.database import init_db


configure_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_pool.start()
    redis_client = await redis_pool.get_pool()

    # Test Redis connection
    try:
        await redis_client.set("test_key", "test_value")
        test_value = await redis_client.get("test_key")
        logger.info(f"Redis test: {test_value}")
    except Exception as e:
        logger.error(f"Redis connection test failed: {e}")

    app.state.redis_pool = redis_pool
    
    await init_db()

    yield

    await redis_pool.stop()  # Close Redis connection pool


app = FastAPI(
    name=config.APP_NAME,
    description=config.PROJECT_DESCRIPTION,
    version=config.PROJECT_VERSION,
    lifespan=lifespan,
)

graphql_app = GraphQLRouter(schema)

app.add_middleware(
    CorrelationIdMiddleware,
    header_name="X-Request-ID",
    update_request_header=True,
    generator=lambda: uuid4().hex,
    validator=is_valid_uuid4,
    transformer=lambda a: a,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def example_endpoint():
    return {"message": "root"}


app.include_router(api_router, prefix="/api/v1")
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
