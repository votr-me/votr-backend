from app.api.routes import api_router
from contextlib import asynccontextmanager
from app.core.config import config
from app.core.logging_config import configure_logging
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi.middleware.cors import CORSMiddleware
from asgi_correlation_id.middleware import is_valid_uuid4
from fastapi import FastAPI, Request, Depends
from fastapi_limiter.depends import RateLimiter

from uuid import uuid4
import logging
from fastapi_limiter import FastAPILimiter
from app.services import (
    open_secrets_async_client,
    fec_async_client,
    congress_async_api_client,
    geocodio_async_client
)
from app.core.redis import redis_pool


configure_logging()
logger = logging.getLogger(__name__)
custom_callback = None 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Set up phase: Initialize Redis connection and async services
    await redis_pool.start()  # Initialize Redis connection pool
    await FastAPILimiter.init(
        redis=await redis_pool.get_pool(),
        prefix="fastapi-limiter"
    )

    congress_client = congress_async_api_client
    base_client = fec_async_client
    opensecrets_client =open_secrets_async_client
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
    lifespan=lifespan
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

@app.get("/", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def example_endpoint(request: Request):
    return {"message": "root"}

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
