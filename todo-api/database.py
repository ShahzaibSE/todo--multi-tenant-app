from sqlalchemy import create_egine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

connection_string: str = os.environ.get('SQLALCHEMY_DATABASE_URL')

# Database connection string
SQLALCHEMY_DATABASE_URL: str = connection_string if connection_string == "" else "<Place your connection string>"

engine = create_egine(SQLALCHEMY_DATABASE_URL)
# Creating database session.
SessionLoc = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()