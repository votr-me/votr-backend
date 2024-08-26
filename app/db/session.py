from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from app.core.config import config

# Ensure DATABASE_URL uses the asyncpg driver
DATABASE_URL = config.DATABASE_URL

# Create the async engine with optimizations for connection pooling and future-proofing
engine = create_async_engine(
    DATABASE_URL,
    echo=config.testing,
    future=True,
    pool_pre_ping=True,  # Ensures connections are valid before use
    pool_recycle=1800,  # Recycle connections after 30 minutes to avoid stale connections
    pool_size=10,  # Set an appropriate pool size based on your workload
    max_overflow=20,  # Allows up to 20 additional connections to be created beyond pool_size
    poolclass=NullPool
    if config.testing
    else None,  # Disable pooling in testing to avoid side effects
)

# Create the async session factory with optimized settings
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,  # Disable autoflush to reduce unnecessary queries during transaction commits
    autocommit=False,  # Explicitly manage transactions to ensure consistency and clarity
)


# Dependency
async def get_session() -> AsyncSession:
    """Yield an async session for use in endpoints."""
    async with async_session() as session:
        try:
            yield session
        finally:
            # Ensure session is closed after use to release resources back to the pool
            await session.close()
