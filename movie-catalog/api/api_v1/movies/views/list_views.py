from fastapi import (
    APIRouter,
    status,
)

from api.api_v1.movies.crud import storage
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
def read_movies_list() -> list[Movie]:
    return storage.get()


@router.post(
    "/",
    response_model=MovieCreate,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: MovieCreate,
) -> Movie:
    return storage.create(movie_create)
