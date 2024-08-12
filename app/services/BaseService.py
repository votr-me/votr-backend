
import json
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.redis import RedisPool
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class BaseService:
    def __init__(self, db: AsyncSession, redis: RedisPool, crud_class):
        self.db = db
        self.redis = redis
        self.crud = crud_class

    async def get_cached_result(self, key: str):
        cached_result = await self.redis.get(key)
        if cached_result:
            logger.debug(f"Cache hit for {key}")
            return json.loads(cached_result)
        return None

    async def cache_result(self, key: str, result: dict, expire: int = 3600):
        await self.redis.set(key, json.dumps(result), expire=expire)
        logger.debug(f"Cache set for {key}")