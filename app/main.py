from fastapi import FastAPI

from app.api.routes.api import router as api_router
from app.core.config import settings

PROJECT_NAME = settings.PROJECT_NAME
DEBUG = settings.DEBUG
API_PREFIX = settings.API_PREFIX


app = FastAPI(title=PROJECT_NAME, debug=DEBUG)

app.include_router(api_router, prefix=API_PREFIX)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Motivational Quotes API!"}
