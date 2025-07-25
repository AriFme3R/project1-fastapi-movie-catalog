from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.api_v1.movies.crud import storage


@asynccontextmanager
async def lifespan(app: FastAPI):
    # действие до запуска приложения

    # ставим эту функцию на паузу
    # на время работы приложения
    yield
    # выполняем завершение работы
    # закрываем соединения, финально сохраняем файлы
