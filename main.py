from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
import os
import uvicorn
import requests

from core.db import SessionLocal, database
from routes import routes

a = os.environ
tags_metadata = [
    {
        "name": "Prepare data",
        "description": "Operations with text , which can prepare your db for search",
    },
    {
        "name": "Task",
        "description": "Required methods",
    },
]

app = FastAPI(redoc_url='/redocs',
              title="Test",
              description="This is a test project, with auto docs for the API and everything",
              version="1.0.0",
              openapi_tags=tags_metadata
              )


@app.on_event("startup")
async def startup():
    await database.connect()
    print("req.status_code")


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get('/')
def get_main():
    return {'test': 'test'}


app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
