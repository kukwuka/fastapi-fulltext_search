import shutil
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from core.utils import get_db
from .services import get_text_list, create_text, serch_text, import_data_fromcsv_topostgres,delete_text
from .schemas import TextBase, TextList, TextCreate



router = APIRouter()


@router.get("/", response_model = List[TextList])
def get_text_list_request(db: Session = Depends(get_db)):
    return get_text_list(db)


@router.post("/", status_code=201)
def create_text_request(item: TextCreate, db: Session = Depends(get_db)):
    return create_text(db, item)


@router.post("/serch/{search_text}", response_model = List[TextList])
def serch_text_request(search_text: str, db: Session = Depends(get_db)):
    return serch_text(search_text, db)


@router.post("/csv", status_code = 201)
def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    with open(f'{file.filename}', "r") as buffer:
        import_data_fromcsv_topostgres(buffer,db)
    return {"file_name": "Good"}


@router.delete("delete/{text_id}", status_code = 204)
def delete_text_request(text_id:int, db: Session = Depends(get_db)):
    delete_text(text_id, db)
    return