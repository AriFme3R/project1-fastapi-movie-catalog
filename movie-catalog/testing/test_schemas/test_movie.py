from unittest import TestCase

from schemas.movie import (
    Movie,
    MovieCreate,
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
