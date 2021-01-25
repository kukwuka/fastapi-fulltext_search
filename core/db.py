from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import  configure_mappers, sessionmaker
from sqlalchemy_searchable import make_searchable
from databases import Database


import sqlalchemy as sa


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:yunis@localhost/fulltext"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sa.orm.configure_mappers()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database = Database(SQLALCHEMY_DATABASE_URL)

Base: DeclarativeMeta = declarative_base()

make_searchable(Base.metadata)