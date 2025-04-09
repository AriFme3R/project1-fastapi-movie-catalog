import logging

from fastapi import (
    HTTPException,
    BackgroundTasks,
    Request,
)
from starlette import status

from .crud import storage
from schemas.movie import Movie

logger = logging.getLogger(__name__)

UNSAFE_METHOD = frozenset(
    [
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    ]
)


def prefetch_movie(
    slug: str,
) -> Movie:
    movie: Movie | None = storage.get_by_slug(slug=slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} not found",
    )


def save_storage_safe(
    request: Request,
    background_tasks: BackgroundTasks,
):
    yield
    if request.method in UNSAFE_METHOD:
        logger.info("Add background task to save storage")
        background_tasks.add_task(storage.save_state)
