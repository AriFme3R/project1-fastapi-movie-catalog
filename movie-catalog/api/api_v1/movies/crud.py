import logging

from pydantic import BaseModel, ValidationError
from redis import Redis

from core import config
from core.config import MOVIES_STORAGE_FILEPATH
from schemas.movie import (
    Movie,
    MovieCreate,
    MovieUpdate,
    MoviePartialUpdate,
)

logger = logging.getLogger(__name__)

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_FOR_MOVIES,
    decode_responses=True,
)


class MoviesStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def save_state(self):
        MOVIES_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))
        logger.info("Saved movies storage file.")

    @classmethod
    def from_state(cls):
        if not MOVIES_STORAGE_FILEPATH.exists():
            logger.info("Movies storage file does not exist.")
            return MoviesStorage()
        return cls.model_validate_json(MOVIES_STORAGE_FILEPATH.read_text())

    def init_storage_from_state(self) -> None:
        try:
            data = MoviesStorage.from_state()
        except ValidationError:
            self.save_state()
            logger.warning("Rewritten storage file.")
            return

        self.slug_to_movie.update(
            data.slug_to_movie,
        )
        logger.warning("Recovered data from storage file.")

    def get(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create(self, movie: MovieCreate) -> Movie:
        movie = Movie(
            **movie.model_dump(),
        )
        redis.hset(
            name=config.REDIS_MOVIES_HASH_NAME,
            key=movie.slug,
            value=movie.model_dump_json(),
        )
        logger.info("Movie created %s", movie)
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_movie.pop(slug, None)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slug(slug=movie.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ) -> Movie:
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        return movie


storage = MoviesStorage()
