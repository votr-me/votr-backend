from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from app.core.config import config
from app.db.models.base_model import BaseModel

DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    future=True,
)

async def init_db():
    async with engine.begin() as conn:
        # Set the search path if needed
        await conn.execute(text("SET search_path TO public"))
        
        # Create all tables
        await conn.run_sync(BaseModel.metadata.create_all)

async def close_db():
    await engine.dispose()
