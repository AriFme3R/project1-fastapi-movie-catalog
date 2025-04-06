from typing import Annotated

from annotated_types import (
    Len,
    MaxLen,
)

from pydantic import BaseModel

DescriptionString = Annotated[
    str,
    MaxLen(500),
]


class MovieBase(BaseModel):
    title: str
    year: int
    duration: int
    description: DescriptionString = ""


class MovieCreate(MovieBase):
    """Модель для создания фильма"""

    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]


class MovieUpdate(MovieBase):
    """
    Модель для обновления информации о фильме
    """

    description: DescriptionString


class MoviePartialUpdate(MovieBase):
    """
    Модель для частичного обновления информации о фильме
    """

    title: str | None = None
    year: int | None = None
    duration: int | None = None
    description: DescriptionString | None = None

class MovieRead(MovieBase):
    """
    Модель для чтения данных о фильме
    """
    slug: str


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
    notes: str
