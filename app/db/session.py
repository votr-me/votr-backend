from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import config

# Ensure DATABASE_URL uses the asyncpg driver
DATABASE_URL = config.DATABASE_URL

# Create the async engine
engine = create_async_engine(DATABASE_URL, echo=config.testing, future=True)

# Create the async session
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Dependency
async def get_db():
    async with async_session() as session:
        yield session
