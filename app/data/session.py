from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from app.core.config.config import config
from sqlalchemy.pool import NullPool

DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Set to True to enable SQL query logging
    poolclass=NullPool,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Yield an async session for database interaction.
    Dependency to get the current database session for each reques
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()  # Ensure that the session is closed after use
