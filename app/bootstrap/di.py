from functools import lru_cache
from punq import Container, Scope

from app.infrastructure.logger.base import ILogger
from app.infrastructure.logger.factory import create_logger_dependency
from app.settings.config import Settings
from app.settings.config import settings


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


# Initialize the dependency injection container
def _init_container() -> Container:
    container: Container = Container()

    # Register global settings
    container.register(
        Settings,
        instance=settings,
        scope=Scope.singleton,
    )

    # Register logger
    container.register(
        ILogger,
        factory=create_logger_dependency,
        scope=Scope.singleton,
    )

    return container
