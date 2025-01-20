from functools import lru_cache
from app.infrastructure.jwt.base import BaseJWTProcessor
from app.infrastructure.jwt.config import JWTConfig
from app.infrastructure.jwt.jwt_processor import PyJWTProcessor
from app.settings.config import settings


@lru_cache(1)
def py_jwt_processor_factory() -> BaseJWTProcessor:
    jwt_config: JWTConfig = JWTConfig(
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM,
    )

    return PyJWTProcessor(jwt_config)