from functools import lru_cache
import logging
import sys

from app.infrastructure.logger.base import ILogger
from app.infrastructure.logger.logger import logger_factory


@lru_cache(1)
def create_logger_dependency() -> ILogger:
    common_logger: logging.Logger = logger_factory(
        name="common",
        level=logging.INFO,
        stream=sys.stdout,
    )
    error_logger: logging.Logger = logger_factory(
        name="error",
        level=logging.ERROR,
        stream=sys.stderr,
    )
    return logging.Logger(logger=common_logger, error_logger=error_logger)