from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import config

# Replace this with your actual database connection string
SQLALCHEMY_DATABASE_URL = "postgresql://your_user:your_password@localhost:5432/votr" 

engine = create_engine(config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()