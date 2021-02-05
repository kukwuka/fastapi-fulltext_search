from fastapi.testclient import TestClient
from httpx import AsyncClient
from os.path import dirname, abspath
import pytest
import sys

from main import app
from core.db import database

path = dirname(abspath(__file__))
sys.path.append(path)

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200




@pytest.mark.asyncio
async def test_root():
    await database.connect()
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("http://127.0.0.1:8000/text_api/", json={
            "created_date": "2021-02-05T12:54:13.150Z",
            "rubrics": "string",
            "text": "string"
        })
    await database.disconnect()
    assert response.status_code == 201

# @pytest.mark.asyncio
# async def test_root():
#     await database.connect()
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("http://127.0.0.1:8000/text_api/", json={
#             "created_date": "2021-02-05T12:54:13.150Z",
#             "rubrics": "string",
#             "text": "string"
#         })
#     await database.disconnect()
#     assert response.status_code == 201

# def test_get_main():
#     response = client.post("http://127.0.0.1:8000/text_api/", json={
#         "created_date": "2021-02-05T12:54:13.150Z",
#         "rubrics": "string",
#         "text": "string"
#     },
#
#                            )
#     assert response.status_code == 200
#     client.post()
# def test_get_main_main():
#     response = client.get("http://0.0.0.0:8000/text_api/")
#     assert response.status_code == 200
