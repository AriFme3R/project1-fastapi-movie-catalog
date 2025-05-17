import secrets
from abc import (
    ABC,
    abstractmethod,
)

from redis import Redis

from core import config


redis_tokens = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_FOR_TOKENS,
    decode_responses=True,
)


class AbstractTokensHelper(ABC):
    """
    Что мне нужно от обертки:
    - проверка наличия токена
    - добавление токена в хранилище
    - генерация нового токена
    """

    @abstractmethod
    def token_exists(
        self,
        token: str,
    ) -> bool:
        """
        Check if token exists.
        :param token:
        :return:
        """

    @abstractmethod
    def add_token(
        self,
        token: str,
    ) -> None:
        """
        Save token to storage.
        :param token:
        :return:
        """

    @classmethod
    def generate_token(cls) -> str:
        return secrets.token_urlsafe(16)

    def generate_and_save_token(self) -> str:
        token = self.generate_token()
        self.add_token(token)
        return token
