import logging
import sys
from functools import lru_cache
from typing import TextIO

from infrastructure.logger.base import ILogger


class Logger(ILogger):

    logger: logging.Logger
    error_logger: logging.Logger

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str) -> None:
        self.error_logger.error(message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)


def logger_factory(name: str, level: int, stream: TextIO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(stream=stream)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    if handler not in logger.handlers:
        logger.addHandler(handler)

    return logger



