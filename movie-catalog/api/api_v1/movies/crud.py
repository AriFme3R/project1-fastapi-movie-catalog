from pydantic import BaseModel

from schemas.movie import (
    Movie,
    MovieCreate,
    MovieUpdate,
    MoviePartialUpdate,
)


class MoviesStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create(self, movie: MovieCreate) -> Movie:
        movie = Movie(
            **movie.model_dump(),
        )
        self.slug_to_movie[movie.slug] = movie
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

storage.create(
    MovieCreate(
        slug="Чтиво",
        title="Криминальное чтиво",
        description="Двое бандитов Винсент Вега и Джулс Винфилд ведут философские беседы в перерывах между разборками и решением проблем с должниками криминального босса Марселласа Уоллеса.",
        year=1995,
        duration=154,
    ),
)

storage.create(
    MovieCreate(
        slug="Рассвет",
        title="От заката до рассвета",
        description="Спасаясь от полиции после ограбления банка, два брата-преступника берут в заложники священника с двумя детьми и бегут в Мексику. Там они должны дождаться подельника, а для этого всей компании нужно переждать ночь в баре дальнобойщиков.",
        year=1995,
        duration=108,
    ),
)

storage.create(
    MovieCreate(
        slug="Убл",
        title="Бесславные ублюдки",
        description="Вторая мировая война. В оккупированной немцами Франции группа американских солдат-евреев наводит страх на нацистов, жестоко убивая и скальпируя солдат.",
        year=2009,
        duration=153,
    ),
)
