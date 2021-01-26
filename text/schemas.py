from pydantic import BaseModel
from datetime import datetime


class TextBase(BaseModel):
    created_date: datetime
    rubrics: str
    text: str

    class Config:
        orm_mode = True


class TextList(TextBase):
    id: int


class TextDetail(TextBase):
    id: int


class TextCreate(TextBase):
    pass
