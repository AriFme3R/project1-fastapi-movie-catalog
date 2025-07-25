from abc import ABC, abstractmethod

import secrets


class AbstractTokensHelper(ABC):
    """
    Что мне нужно от обертки:
    - проверка наличия токена
    - добавление токена в хранилище
    - генерация нового токена
    """

    """
    Абстрактный базовый класс для работы с токенами.
    Определяет контракт для проверки, добавления и генерации токенов.
    """

    @abstractmethod
    def token_exists(
        self,
        token: str,
    ) -> bool:
        """
        Проверяет, существует ли токен в хранилище.

        Args:
            token (str): Токен для проверки.

        Returns:
            bool: True, если токен существует, иначе False.
        """
        pass

    @abstractmethod
    def add_token(
        self,
        token: str,
    ) -> None:
        """
        Добавляет токен в хранилище.

        Args:
            token (str): Токен для добавления.
        """
        pass

    @abstractmethod
    def get_tokens(self) -> list[str]:
        """
        Выводит список всех токенов.

        Returns:
            list[str]: Список токенов.
        """
        pass

    @classmethod
    def generate_token(cls) -> str:
        """
        Генерирует безопасный случайный токен.

        Returns:
            str: Сгенерированный токен.
        """
        return secrets.token_urlsafe(16)

    def generate_and_save_token(self) -> str:
        """
        Генерирует новый токен и сохраняет его в хранилище.

        Returns:
            str: Сгенерированный токен.
        """
        token = self.generate_token()
        self.add_token(token)
        return token
