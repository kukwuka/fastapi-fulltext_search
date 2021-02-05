from fastapi import APIRouter


from text import text

routes = APIRouter()

routes.include_router(text.router , prefix = "/text_api")
