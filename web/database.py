import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ

# for docker
db_url = environ.get('DATABASE_URL')

# for PC
# db_url = 'postgresql://user:dbdb192618@localhost:15432/db'

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
