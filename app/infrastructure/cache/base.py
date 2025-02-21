from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Generic,
    TypeVar,
)

from redis.asyncio import Redis


KeyValue = TypeVar("KeyValue")
Value = TypeVar("Value")


class ICacheService(ABC, Generic[KeyValue, Value]):

    redis: Redis

    @abstractmethod
    async def get_value(self, key_value: KeyValue) -> Value | None:
        """Получить значение по ключу."""
        ...

    @abstractmethod
    async def set_value(self, key_value: KeyValue, value: Value) -> None:
        """Сохранить значение по ключу."""
        ...
