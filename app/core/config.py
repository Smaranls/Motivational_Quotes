import sys
import logging
from loguru import logger
from pydantic_settings import BaseSettings
from app.core.logging import InterceptHandler

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    VERSION: str = "1.0"
    DEBUG: bool = True
    PROJECT_NAME: str = "Motivational Quotes API"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

# Logging configuration
LOGGING_LEVEL = logging.DEBUG if settings.DEBUG else logging.INFO

logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)],
    level=LOGGING_LEVEL,
)

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
