import csv
from core.db import database
from datetime import datetime
from sqlalchemy_searchable import search
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException
from pathlib import Path
from fastapi import UploadFile

from .models import Text, texts
from .schemas import TextCreate


async def get_text_list():
    query = texts.select().limit(20)
    query_fetch = await database.fetch_all(query=query)
    return [dict(result) for result in query_fetch]


async def create_text(item: TextCreate):
    create_query = texts.insert().values(**item.dict())
    create_query_fetch_and_id = await database.execute(create_query)
    return {**item.dict(), "id": create_query_fetch_and_id}


def serch_text(search_text: str, db: Session):
    query = db.query(Text)
    query = search(query, search_text).limit(20)
    get_query = query.all()
    return get_query


async def import_data_from_csv_to_postgres(file: UploadFile) -> List:
    file_is_csv = Path(file.filename).suffix == '.csv'
    if not file_is_csv:
        raise HTTPException(status_code=418, detail="couldn't find text")

    content = await file.read()
    with open(f'upload/{file.filename}', "wb") as buffer:
        buffer.write(content)

    with open(str(buffer.name), 'r') as buffer:
        csv_reader = csv.reader(buffer)
        try:
            gen = (i for i in csv_reader)
            next(gen)
            created_text_id = []
            for line in gen:
                text = line[0]
                # invert str to date, because asyncpg can't convert str to datetime,
                # But if we use standart sqlalchemy,
                # we can pass str
                created_date = datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S')
                rubrics = line[2]
                create_line_db_query = texts.insert().values(text=text, created_date=created_date, rubrics=rubrics)
                create_line_db_query_fetch_and_id = await database.execute(create_line_db_query)
                created_text_id.append(create_line_db_query_fetch_and_id)
        except Exception:
            raise HTTPException(status_code=418, detail="couldn't find text")
    return created_text_id


async def delete_text(text_id: int):
    find_query = texts.select().where(texts.c.id == text_id)
    find_query_fetch = await database.fetch_one(query=find_query)
    print(find_query_fetch)
    if find_query_fetch is None:
        return None
    delete_query = texts.delete().where(texts.c.id == text_id)
    delete_query_fetch = await database.execute(delete_query)
    return {**find_query_fetch}


async def find_text(text_id: int):
    find_query = texts.select().where(texts.c.id == text_id)
    find_query_fetch = await database.fetch_one(query=find_query)
    if find_query_fetch is None:
        return None
    return {**find_query_fetch}
