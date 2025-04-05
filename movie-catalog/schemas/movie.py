from typing import Annotated

from annotated_types import (
    Len,
    MaxLen,
)

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    year: int
    duration: int
    description: Annotated[
        str,
        MaxLen(500),
    ] = ""


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

    description: Annotated[
        str,
        MaxLen(200),
    ]


class Movie(MovieBase):
    """
    Модель фильма
    """

    slug: str
