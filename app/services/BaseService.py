import json
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.redis import RedisPool
from fastapi import HTTPException

from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")


class BaseService:
    def __init__(self, db: AsyncSession, redis: RedisPool, crud_class, *args, **kwargs):
        self.db = db
        self.redis = redis
        # Instantiate the CRUD class with additional arguments
        self.crud = crud_class(db, *args, **kwargs)

    async def get_cached_result(self, key: str):
        cached_result = await self.redis.get(key)
        if cached_result:
            return json.loads(cached_result)
        return None

    async def cache_result(self, key: str, result: dict, expire: int = 3600):
        await self.redis.set(key, json.dumps(result), expire=expire)

    async def fetch_and_validate(
        self, fetch_method, *args, error_message: str, **kwargs
    ):
        result = await fetch_method(*args, **kwargs)
        if not result:
            logger.info(error_message)
            raise HTTPException(status_code=404, detail=error_message)
        return result
