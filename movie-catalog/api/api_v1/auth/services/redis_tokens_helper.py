__all__ = ("redis_tokens",)

from redis import Redis

from api.api_v1.auth.services.tokens_helper import AbstractTokensHelper
from core import config


class RedisTokensHelper(AbstractTokensHelper):
    """
    Реализация обёртки для работы с токенами в Redis.
    Использует множество (set) для хранения токенов.
    """

    def __init__(
        self,
        host: str,
        port: int,
        db: int,
        tokens_set_name: str,
    ) -> None:
        """
        Инициализирует соединение с Redis
        и задаёт имя множества для токенов.

        Args:
            host (str): Хост Redis.
            port (int): Порт Redis.
            db (int): Номер базы данных Redis.
            tokens_set_name (str): Имя множества для хранения токенов.
        """
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )
        self.tokens_set_name = tokens_set_name

    def token_exists(self, token_to_check: str) -> bool:
        """
        Проверяет, существует ли токен в множестве Redis.

        Args:
            token_to_check (str): Токен для проверки.

        Returns:
            bool: True, если токен существует, иначе False.
        """
        return bool(
            self.redis.sismember(
                self.tokens_set_name,
                token_to_check,
            )
        )

    def add_token(self, token_to_add: str) -> None:
        """
        Добавляет токен в множество Redis.

        Args:
            token_to_add (str): Токен для добавления.
        """
        self.redis.sadd(
            self.tokens_set_name,
            token_to_add,
        )

    def get_tokens(self) -> list[str]:
        """
        Выводит список всех токенов.

        Returns:
            list[str]: Список токенов.
        """
        return list(
            self.redis.smembers(name=self.tokens_set_name),
        )

    def delete_token(self, token: str) -> None:
        self.redis.srem(
            self.tokens_set_name,
            token,
        )


redis_tokens = RedisTokensHelper(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_FOR_TOKENS,
    tokens_set_name=config.REDIS_TOKENS_SET_NAME,
)
