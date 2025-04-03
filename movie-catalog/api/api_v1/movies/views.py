from random import randint

from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
)

from .crud import MOVIES
from .dependencies import prefetch_movie
from schemas.movie import (
    Movie,
    MovieCreate,
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[Movie],
)
def read_movies_list():
    return MOVIES


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(movie_create: MovieCreate) -> Movie:
    return Movie(
        id=randint(4, 100),
        title=movie_create.title,
        description=movie_create.description,
        year=movie_create.year,
        duration=movie_create.duration,
    )


@router.get(
    "/{movie_id}/",
    response_model=Movie,
)
def read_movie_details(
    movie_details: Annotated[
        Movie,
        Depends(prefetch_movie),
    ],
) -> Movie:
    return movie_details
