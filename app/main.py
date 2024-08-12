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
from app.db.session import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.redis import get_redis_pool, RedisPool
from fastapi_limiter import FastAPILimiter


configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_pool.start()
    redis_client = await redis_pool.get_pool()
    app.state.redis_pool = redis_pool

    await init_db()

    await FastAPILimiter.init(redis_client)

    yield

    await redis_pool.stop()  # Close Redis connection pool


async def get_context(
    db: AsyncSession = Depends(get_db), redis: RedisPool = Depends(get_redis_pool)
):
    return {"db": db, "redis": redis}


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
