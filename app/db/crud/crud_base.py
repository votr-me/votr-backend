from typing import Generic, List, Optional, Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import DeclarativeBase, selectinload
from app.db.models.base_model import BaseModel


ModelType = TypeVar("ModelType", bound=DeclarativeBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_by_bioguide_id(
        self, db: AsyncSession, bioguide_id: int, load_relationships: bool = False
    ) -> Optional[ModelType]:
        """Get a single item by ID, optionally loading relationships."""
        query = select(self.model).filter(self.model.bioguide_id == bioguide_id)
        if load_relationships:
            for relationship_name in self.model.__mapper__.relationships.keys():
                query = query.options(
                    selectinload(getattr(self.model, relationship_name))
                )
        result = await db.execute(query)
        return result.scalars().first()

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        """Get multiple items with optional pagination."""
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()

    async def filter_by(
        self,
        db: AsyncSession,
        filter_conditions: dict,
        load_relationships: bool = False,
    ) -> List[ModelType]:
        """Retrieve a list of items based on specified filter conditions."""
        query = select(self.model)
        for key, value in filter_conditions.items():
            query = query.filter(getattr(self.model, key) == value)
        if load_relationships:
            for relationship_name in self.model.__mapper__.relationships.keys():
                query = query.options(
                    selectinload(getattr(self.model, relationship_name))
                )
        result = await db.execute(query)
        return result.scalars().all()
