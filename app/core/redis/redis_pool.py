import logging
import redis.asyncio as redis
from app.core.config.config import config
import asyncio
from contextlib import asynccontextmanager

# Configure logging once at the module level
logger = logging.getLogger("app")


class RedisPool:
    _instance = None
    _lock = asyncio.Lock()  # Ensure thread-safety in async environment

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, url: str = None, max_connections: int = 10):
        if not hasattr(self, "pool"):
            self.url = url or config.REDIS_URL
            self.max_connections = max_connections
            self.pool = None

    async def start(self):
        if not self.pool:
            async with RedisPool._lock:  # Ensure only one instance initializes the pool
                if not self.pool:  # Double check inside the lock
                    try:
                        self.pool = await redis.from_url(
                            self.url,
                            encoding="utf-8",
                            decode_responses=True,
                            max_connections=self.max_connections,
                        )
                        logger.info("Redis connection pool established")
                    except redis.RedisError as e:
                        logger.error(f"Failed to create Redis connection pool: {e}")
                        raise e

    async def stop(self):
        if self.pool:
            try:
                await self.pool.close()
                self.pool = None
                logger.info("Redis connection pool closed")
            except redis.RedisError as e:
                logger.error(f"Error closing Redis connection pool: {e}")

    async def get_pool(self):
        if not self.pool:
            await self.start()
        return self.pool

    async def get(self, key: str):
        pool = await self.get_pool()
        try:
            return await pool.get(key)
        except redis.RedisError as e:
            logger.error(f"Error getting key '{key}' from Redis: {e}")
            return None

    async def set(self, key: str, value: str, expire: int = 3600):
        pool = await self.get_pool()
        try:
            await pool.set(key, value, ex=expire)
            logger.debug(f"Key '{key}' set in Redis with expiration {expire} seconds")
        except redis.RedisError as e:
            logger.error(f"Error setting key '{key}' in Redis: {e}")


redis_pool = RedisPool(config.REDIS_URL)


async def get_redis_pool() -> RedisPool:
    return redis_pool


@asynccontextmanager
async def redis_connection():
    pool = await redis_pool.get_pool()
    try:
        yield pool
    finally:
        pass  # No need to explicitly close the pool here, managed by RedisPool class
