from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from app.core.config.config import config


DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to True if you want to log all the SQL queries
    pool_size=20,  # Set the pool size for handling concurrent connections
    max_overflow=10,  # Allow up to 10 overflow connections during spikes
    future=True,  # SQLAlchemy 2.0 style
)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,  # Ensure that we are using async sessions
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
