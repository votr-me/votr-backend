from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import text
from app.core.config import config
from app.db.models.base_model import BaseModel

DATABASE_URL = config.DATABASE_URL

# Create the async engine with optimal settings
engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=config.DBLOGS,  # Set to True for debugging purposes if needed
    future=True,
    pool_size=10,  # Adjust pool size according to your app's needs
    max_overflow=20,  # Allow extra connections beyond the pool_size
    pool_timeout=30,  # Timeout for acquiring a connection from the pool
)


async def init_db():
    """Initialize the database, creating all tables."""
    async with engine.begin() as conn:
        # Optional: Set the search path if working with schemas
        await conn.execute(text("SET search_path TO public"))

        # Create all tables defined in BaseModel
        await conn.run_sync(BaseModel.metadata.create_all)


async def close_db():
    """Dispose of the engine to clean up connections."""
    await engine.dispose()
