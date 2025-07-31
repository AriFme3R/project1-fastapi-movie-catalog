from unittest import TestCase

from schemas.movie import (
    Movie,
    MovieCreate,
    MoviePartialUpdate,
    MovieUpdate,
)


class MovieCreateTestCase(TestCase):
    def test_movie_can_be_created_from_create_schema(self) -> None:
        movie_in = MovieCreate(
            slug="some-slug",
            title="some-title",
            year=2025,
            duration=90,
            description="some-description",
        )

        movie = Movie(**movie_in.model_dump())

        self.assertEqual(movie_in.slug, movie.slug)
        self.assertEqual(movie_in.title, movie.title)
        self.assertEqual(movie_in.year, movie.year)
        self.assertEqual(movie_in.duration, movie.duration)
        self.assertEqual(movie_in.description, movie.description)


class MovieUpdateTestCase(TestCase):
    def test_movie_can_be_updated_from_update_schema(self) -> None:
        movie_in = MovieUpdate(
            title="some-title",
            year=2025,
            duration=90,
            description="some-description",
        )

        movie = Movie(
            **movie_in.model_dump(),
            slug="some-slug",
        )

        self.assertEqual(movie_in.title, movie.title)
        self.assertEqual(movie_in.year, movie.year)
        self.assertEqual(movie_in.duration, movie.duration)
        self.assertEqual(movie_in.description, movie.description)


class MoviePartialUpdateTestCase(TestCase):
    def test_empty_partial_update_from_partial_update_schema(self) -> None:
        movie_in = MoviePartialUpdate()

        movie = Movie(
            **movie_in.model_dump(exclude_unset=True),
            slug="some-slug",
            title="some-title",
            year=2025,
            duration=90,
            description="some-description",
        )

        self.assertEqual("some-title", movie.title)
        self.assertEqual(2025, movie.year)
        self.assertEqual(90, movie.duration)
        self.assertEqual("some-description", movie.description)

    def test_movie_can_be_partial_update_from_partial_update_schema(
        self,
    ) -> None:
        movie_in = MoviePartialUpdate(
            title="another-title",
            year=2020,
        )

        movie = Movie(
            **movie_in.model_dump(exclude_unset=True),
            slug="some-slug",
            duration=90,
            description="some-description",
        )

        self.assertEqual(movie_in.title, movie.title)
        self.assertEqual(movie_in.year, movie.year)

        self.assertEqual(90, movie.duration)
        self.assertEqual("some-description", movie.description)
