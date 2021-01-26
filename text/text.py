from fastapi import APIRouter, Depends, UploadFile, File
from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.utils import get_db
from .services import get_text_list, create_text, serch_text, save_and_import_csv_data, delete_text, find_text
from .schemas import TextList, TextCreate, TextDetail

router = APIRouter()


# changed
@router.get("/", response_model=List[TextList], tags=["Prepare data"])
async def get_text_list_request():
    """Get all texts"""
    return await get_text_list()


# changed
@router.post("/", status_code=201, tags=["Prepare data"])
async def create_text_request(item: TextCreate):
    """Create text"""
    return await create_text(item)


@router.get("/serch", response_model=List[TextList], tags=["Task"])
def serch_text_request(search_text: str, db: Session = Depends(get_db)):
    """Serch text"""
    return serch_text(search_text, db)


@router.post("/csv", status_code=201, tags=["Prepare data"])
async def upload_csv(file: UploadFile = File(...)):
    print(file)
    texts_ids = await save_and_import_csv_data(file)
    return {"file_name": texts_ids}


@router.delete("/delete/{text_id}", response_model=TextDetail, tags=["Task"])
async def delete_text_request(text_id: int):
    """Delete with id"""
    deleted_text = await delete_text(text_id)
    if deleted_text is None:
        raise HTTPException(status_code=418, detail="couldn't find text")
    return deleted_text


@router.get("/{text_id}", response_model=TextDetail, tags=["Prepare data"])
async def get_text(text_id: int):
    """Find text with id"""
    finded_text = await find_text(text_id)
    if finded_text is None:
        raise HTTPException(status_code=418, detail="couldn't find text")
    return finded_text
