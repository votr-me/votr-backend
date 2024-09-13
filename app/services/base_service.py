from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic
import logging

# Define a generic type for repositories
T = TypeVar("T")


class BaseService(Generic[T]):
    """
    Base service class that provides shared functionality for all services.

    Attributes:
        db: The SQLAlchemy async session.
        logger: Logger for the service.
    """

    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = logging.getLogger(self.__class__.__name__)

    async def commit(self) -> None:
        """Commit the current database transaction."""
        try:
            await self.db.commit()
        except Exception as e:
            self.logger.error(f"Error during commit: {e}")
            await self.db.rollback()
            raise e

    async def rollback(self) -> None:
        """Rollback the current database transaction."""
        try:
            await self.db.rollback()
        except Exception as e:
            self.logger.error(f"Error during rollback: {e}")
            raise e

    def log_info(self, message: str) -> None:
        """Log informational messages."""
        self.logger.info(message)

    def log_error(self, message: str) -> None:
        """Log error messages."""
        self.logger.error(message)
