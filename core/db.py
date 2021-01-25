from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, configure_mappers
from sqlalchemy_searchable import make_searchable


import sqlalchemy as sa


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:yunis@localhost/fulltext"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sa.orm.configure_mappers()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

make_searchable(Base.metadata)