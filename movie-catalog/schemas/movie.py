from typing import Annotated

from annotated_types import Len

from pydantic import BaseModel


class MovieBase(BaseModel):
    id: int | None = None
    title: str
    description: str
    year: int
    duration: int


class MovieCreate(BaseModel):
    """Модель для создания фильма"""

    title: Annotated[str, Len(min_length=8, max_length=50)]
    description: str
    year: int
    duration: int


class Movie(MovieBase):
    """
    Модель фильма
    """
