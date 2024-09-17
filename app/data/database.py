from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from app.data.models import Base
from app.core.config.config import config

# Create the async engine for the database
DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # Turn off SQL echo in production
    pool_size=20,  # Adjust based on your needs
    max_overflow=10,  # Allow overflow connections for short spikes
    future=True,  # Enable SQLAlchemy 2.0 behavior
)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=sessionmaker,  # AsyncSession if you need session binding
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Function to close the database connection pool, used during shutdown
async def close_db():
    await engine.dispose()
