from app.db import Base

class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {'schema': 'raw'} 