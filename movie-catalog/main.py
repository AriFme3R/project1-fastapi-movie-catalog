import logging

from fastapi import (
    FastAPI,
    Request,
)
from api import router as api_router

from core import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
)

app = FastAPI(
    title="Movie Catalog",
)

app.include_router(api_router)


@app.get("/")
def read_root(
    request: Request,
    name: str = "World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello, {name}!",
        "docs": str(docs_url),
    }
