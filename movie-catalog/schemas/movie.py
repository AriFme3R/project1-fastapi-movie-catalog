from typing import Annotated

from annotated_types import (
    Len,
    MaxLen,
)

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: Annotated[
        str,
        MaxLen(200),
    ] = ""
    year: int
    duration: int


class MovieCreate(MovieBase):
    """Модель для создания фильма"""

    slug: Annotated[
        str,
        Len(min_length=5, max_length=50),
    ]
    title: Annotated[
        str,
        Len(min_length=5, max_length=50),
    ]
    description: str
    year: int
    duration: int


class MovieUpdate(MovieBase):
    """
    Модель для обновления информации о фильме
    """
    description: Annotated[
        str,
        MaxLen(200),
    ]


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
