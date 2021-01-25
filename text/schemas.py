from pydantic import BaseModel
from datetime import datetime


class TextBase(BaseModel):
    date: datetime
    rubricks: str
    text: str

    class Config:
        orm_mode = True


class TextList(TextBase):
    id: int

class TextDetail(TextBase):
    id:int

class TextCreate(TextBase):
    pass
