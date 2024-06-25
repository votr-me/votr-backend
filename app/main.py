from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import config
from app.core.logging_config import configure_logging
from app.core.redis import redis_pool
from app.services import (
    open_secrets_async_client,
    fec_async_client,
    congress_async_api_client,
    geocodio_async_client,
)
from asgi_correlation_id import CorrelationIdMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from contextlib import asynccontextmanager
from uuid import uuid4
import logging

configure_logging()
logger = logging.getLogger(__name__)
custom_callback = None


class DebugRedisBackend(RedisBackend):
    async def get(self, key: str):
        value = await super().get(key)
        logger.debug(f"Cache GET: {key} -> {'Hit' if value else 'Miss'}")
        return value

    async def set(self, key: str, value: str, expire: int = None):
        await super().set(key, value, expire)
        if len(key) > 200:  # Assuming 200 is the max length for your cache keys
            logger.debug(f"Cache SET (Hashed Key): {key} (Expire: {expire}s)")
        else:
            logger.debug(f"Cache SET: {key} (Expire: {expire}s)")

        return value


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

    FastAPICache.init(DebugRedisBackend(redis_client), prefix="fastapi-cache")

    # FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

    await FastAPILimiter.init(
        redis=await redis_pool.get_pool(), prefix="fastapi-limiter"
    )

    congress_client = congress_async_api_client
    base_client = fec_async_client
    opensecrets_client = open_secrets_async_client
    geocodio_client = geocodio_async_client

    app.state.congress_client = congress_client
    app.state.base_client = base_client
    app.state.opensecrets_client = opensecrets_client
    app.state.geocodio_client = geocodio_client
    app.state.redis_pool = redis_pool

    yield

    await FastAPILimiter.close()
    await redis_pool.stop()  # Close Redis connection pool
    await congress_client.close()  # Replace with actual stop/cleanup method
    await base_client.close()  # Replace with actual stop/cleanup method
    await opensecrets_client.close()
    await geocodio_client.close()


app = FastAPI(
    name=config.APP_NAME,
    description=config.PROJECT_DESCRIPTION,
    version=config.PROJECT_VERSION,
    lifespan=lifespan,
)

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


@app.get("/", dependencies=[Depends(RateLimiter(times=100, seconds=60))])
@cache(expire=3600)  # Cache responses for 5 seconds
async def example_endpoint():
    return {"message": "root"}


@app.get("/debug/redis")
async def debug_redis():
    redis = await redis_pool.get_pool()
    await redis.set("test_key", "test_value")
    value = await redis.get("test_key")
    return {"redis_test": value}


@app.get("/debug/redis-keys")
async def debug_redis_keys():
    redis_client = await redis_pool.get_pool()
    keys = await redis_client.keys("fastapi-cache:*")
    return {"cache_keys": keys}


app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
