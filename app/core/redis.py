import redis.asyncio as redis
from app.core.config import config
import logging


logger = logging.getLogger(__name__)


class RedisPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, url: str):
        if not hasattr(self, "pool"):
            self.url = url
            self.pool = None

    async def start(self):
        if not self.pool:
            self.pool = await redis.from_url(
                self.url, encoding="utf-8", decode_responses=True, max_connections=10
            )
            logger.info("Redis connection pool established")

    async def stop(self):
        if self.pool:
            await self.pool.close()
            self.pool = None
            logger.info("Redis connection pool closed")

    async def get_pool(self):
        if not self.pool:
            await self.start()
        return self.pool


redis_pool = RedisPool(config.REDIS_URL)
