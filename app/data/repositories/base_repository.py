from typing import Type, TypeVar, Generic, List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Define a generic type for models
T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, db: AsyncSession, model: Type[T]):
        self.db = db
        self.model = model

    async def get_all(self, limit: int = 10, offset: int = 0) -> List[T]:
        """Fetch paginated records"""
        query = select(self.model).limit(limit).offset(offset)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def create(self, obj_in: T) -> T:
        """Create a new record"""
        self.db.add(obj_in)
        await self.db.commit()
        await self.db.refresh(obj_in)
        return obj_in

    async def update(self, record_id: int, obj_in: Dict[str, Any]) -> Optional[T]:
        """Update an existing record"""
        db_obj = await self.get_by_id(record_id)
        if db_obj:
            for key, value in obj_in.items():
                setattr(db_obj, key, value)
            await self.db.commit()
            await self.db.refresh(db_obj)
        return db_obj

    async def delete(self, record_id: int) -> bool:
        """Delete a record by ID"""
        db_obj = await self.get_by_id(record_id)
        if db_obj:
            await self.db.delete(db_obj)
            await self.db.commit()
            return True
        return False
