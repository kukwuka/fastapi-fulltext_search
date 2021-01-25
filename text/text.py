import shutil
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from fastapi import  HTTPException

from core.utils import get_db
from .services import get_text_list, create_text, serch_text, import_data_fromcsv_topostgres,delete_text
from .schemas import TextBase, TextList, TextCreate, TextDetail



router = APIRouter()

# changed
@router.get("/", response_model = List[TextList])
async def get_text_list_request():
    return await get_text_list()

# changed
@router.post("/", status_code=201)
async def create_text_request(item: TextCreate):
    return await create_text(item)


@router.post("/serch/{search_text}", response_model = List[TextList])
def serch_text_request(search_text: str, db: Session = Depends(get_db)):
    return serch_text(search_text, db)

# changed
@router.post("/csv", status_code = 201)
async def upload_image(file: UploadFile = File(...)):
    try:
        with open(f'{file.filename}', "r") as buffer:
            created_texts_id = await  import_data_fromcsv_topostgres(buffer)
        return {'texts_id': created_texts_id}
    except Exception:
        raise HTTPException(status_code=418, detail="file is incorrect")


@router.delete("/delete/{text_id}", response_model=TextDetail)
async def delete_text_request(text_id:int):
    deleted_text = await delete_text(text_id)
    if deleted_text is None:
        raise HTTPException(status_code=418, detail="couldn't find text")
    return deleted_text