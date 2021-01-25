from sqlalchemy_searchable import search
from sqlalchemy.orm import Session
import csv

from .models import Text,texts
from .schemas import TextCreate


def get_text_list(db: Session):
    query = db.query(Text).limit(1)
    print(query)
    get_query = query.all()
    return get_query


def create_text(db: Session, item: TextCreate):
    text = Text(**item.dict())
    db.add(text)
    db.commit()
    db.refresh(text)
    return text


def serch_text(search_text: str, db: Session):
    query = db.query(Text)
    query = search(query, search_text).limit(20)
    get_query = query.all()
    print(query)
    return get_query


def import_data_fromcsv_topostgres(buffer, db: Session):
    csv_reader = csv.reader(buffer)
    gen = (i for i in csv_reader)
    next(gen)

    for line in gen:
        text = line[0]
        date = line[1]
        rubricks = line[2]
        # line_for_schemas = {'text': 1, 'date': 2, 'rubrics'}
        db_text = Text(text=text, date=date, rubricks=rubricks)
        db.add(db_text)
        db.commit()
        db.refresh(db_text)
        print(1)
    return

def delete_text(text_id: int, db:Session) -> bool:
    choosed_query = Text.query.filter_by(id=text_id).one()

    query = db.delete(choosed_query)
    print(query)
    return