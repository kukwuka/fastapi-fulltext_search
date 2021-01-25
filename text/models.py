from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import sync_trigger

from core.db import Base


class Text(Base):
    __tablename__ = 'text'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=False))
    rubricks = Column(UnicodeText)
    text = Column(UnicodeText)
    search_vector = Column(TSVectorType('text'))


texts = Text.__table__
