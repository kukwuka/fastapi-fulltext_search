from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import configure_mappers, sessionmaker
from sqlalchemy_searchable import make_searchable
from databases import Database
import os

import sqlalchemy as sa

load_dotenv()
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URL =  "postgresql://route_admin:route_admin@localhost:5433/postgres"
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sa.orm.configure_mappers()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database = Database(SQLALCHEMY_DATABASE_URL)

Base: DeclarativeMeta = declarative_base()

make_searchable(Base.metadata)
