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

    # async def create(
    #     self, db: AsyncSession, *, obj_in: CreateSchemaType
    # ) -> ModelType:
    #     """Create a new item."""
    #     obj_in_data = obj_in.dict()
    #     db_obj = self.model(**obj_in_data)
    #     db.add(db_obj)
    #     await db.commit()
    #     await db.refresh(db_obj)
    #     return db_obj

    # async def update(
    #     self, db: AsyncSession, *, db_obj: ModelType, obj_in: UpdateSchemaType
    # ) -> ModelType:
    #     """Update an existing item."""
    #     obj_data = obj_in.dict(exclude_unset=True)
    #     for field in obj_data:
    #         setattr(db_obj, field, obj_data[field])
    #     db.add(db_obj)
    #     await db.commit()
    #     await db.refresh(db_obj)
    #     return db_obj

    # async def delete(self, db: AsyncSession, *, id: int) -> ModelType:
    #     """Delete an item by ID."""
    #     obj = await self.get(db, id)
    #     await db.delete(obj)
    #     await db.commit()
    #     return obj


# from typing import TypeVar, Generic, List, Optional, Type
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.orm import DeclarativeBase

# ModelType = TypeVar("ModelType", bound=DeclarativeBase)


# class CRUDBase(Generic[ModelType]):
#     def __init__(self, model: Type[ModelType]):
#         self.model = model

#     async def get(self, db: AsyncSession, id: int) -> Optional[ModelType]:
#         """Get a single item by ID."""
#         result = await db.execute(select(self.model).filter(self.model.id == id))
#         return result.scalars().first()

#     async def get_multi(
#         self, db: AsyncSession, *, skip: int = 0, limit: int = 100
#     ) -> List[ModelType]:

#         """Get multiple items with optional pagination."""
#         result = await db.execute(select(self.model).offset(skip).limit(limit))
#         return result.scalars().all()

#     async def filter_by(
#         self, db: AsyncSession, filter_conditions: dict
#     ) -> List[ModelType]:
#         """Retrieve a list of items based on specified filter conditions."""
#         query = select(self.model)
#         for key, value in filter_conditions.items():
#             query = query.filter(getattr(self.model, key) == value)
#         result = await db.execute(query)
#         return result.scalars().all()

# class CRUDBase(Generic[ModelType]):
#     def __init__(self, model: ModelType):
#         self.model = model

#     async def get(
#         self, db: AsyncSession, id: int, *, options=None
#     ) -> Optional[ModelType]:
#         query = select(self.model).filter(self.model.id == id)
#         if options:
#             query = query.options(*options)
#         result = await db.execute(query)
#         return result.scalars().first()

#     async def get_multi(
#         self, db: AsyncSession, *, skip: int = 0, limit: int = 100, options=None
#     ) -> List[ModelType]:
#         query = select(self.model).offset(skip).limit(limit)
#         if options:
#             query = query.options(*options)
#         result = await db.execute(query)
#         return result.scalars().all()


# from typing import TypeVar, Generic, List
# from fastapi import HTTPException, status
# from pydantic import BaseModel
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.orm import selectinload  # Import for eager loading

# ModelType = TypeVar("ModelType")
# CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

# class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
#     def __init__(self, model: ModelType):
#         self.model = model

#     async def get(self, db: AsyncSession, id: int, *, options=None) -> ModelType | None:
#         query = select(self.model).filter(self.model.id == id)
#         if options:  # Allow for customizable query options (e.g., eager loading)
#             query = query.options(*options)
#         result = await db.execute(query)
#         return result.scalars().first()

#     async def get_multi(
#         self, db: AsyncSession, *, skip: int = 0, limit: int = 100, options=None
#     ) -> List[ModelType]:
#         query = select(self.model).offset(skip).limit(limit)
#         if options:
#             query = query.options(*options)
#         result = await db.execute(query)
#         return result.scalars().all()

#     async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
#         db_obj = self.model(**obj_in.dict())  # No need for intermediate dict
#         db.add(db_obj)
#         await db.commit()
#         await db.refresh(db_obj)
#         return db_obj

#     async def update(self, db: AsyncSession, *, db_obj: ModelType, obj_in: UpdateSchemaType | dict) -> ModelType:
#         update_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_unset=True)
#         for field, value in update_data.items():  # Iterate directly over update_data
#             setattr(db_obj, field, value)
#         db.add(db_obj)
#         await db.commit()
#         await db.refresh(db_obj)
#         return db_obj

#     async def remove(self, db: AsyncSession, *, id: int) -> ModelType:
#         obj = await self.get(db, id)
#         if not obj:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
#         await db.delete(obj)
#         await db.commit()
#         return obj
