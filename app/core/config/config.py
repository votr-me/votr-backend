import pathlib
from functools import lru_cache
from typing import Optional, Type, ClassVar

from pydantic_settings import BaseSettings
import logging

# Define the root directory

logger = logging.getLogger(__name__)
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent


class BaseConfig(BaseSettings):
    APP_NAME: str = "Votr"
    PROJECT_VERSION: str = "0.0.0"
    ENV_STATE: Optional[str] = None
    PROJECT_DESCRIPTION: Optional[str] = None
    api_v1_str: str = "/api/v1"
    GEOCODIO_BASE_URL: ClassVar[str] = "https://api.geocod.io/v1.7/"
    CACHE_TTL: Optional[int] = 3600
    LOG_LVL: str = "INFO"  # Add LOG_LVL to BaseConfig
    logs_directory: str = "app/logs"
    DEFAULT_TTL: Optional[int] = 3600  # set default caching expiration time to 1 hour

    class Config:
        env_file = ROOT / ".env"
        extra = "ignore"


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    SYNC_DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    logs_directory: str = "app/logs"
    testing: bool = False
    DBLOGS: Optional[bool] = None


class DevConfig(GlobalConfig):
    LOG_LVL: str = "DEBUG"
    testing: bool = True
    DATABASE_URL: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    GEOCODIO_API_KEY: Optional[str] = None
    CONGRESS_GOV_API_KEY: Optional[str] = None
    OPENSECRETS_API_KEY: Optional[str] = None
    CACHE_TTL: Optional[int] = None
    REDIS_URL: Optional[str] = None
    FEC_API_KEY: Optional[str] = None
    USER_SESSION_KEY: Optional[str] = None
    DBLOGS: Optional[bool] = None
    DEFAULT_TTL: Optional[int] = None

    class Config:
        env_prefix = "DEV_"


class ProdConfig(GlobalConfig):
    LOG_LVL: str = "INFO"
    testing: bool = False
    PROD_DBLOGS: Optional[bool] = None

    class Config:
        env_prefix = "PROD"


class TestConfig(GlobalConfig):
    LOG_LVL: str = "TEST"
    testing: bool = True
    TEST_DBLOGS: Optional[bool] = None

    class Config:
        env_prefix = "TEST"


@lru_cache()
def get_config(env_state: Optional[str] = None) -> GlobalConfig:
    """Instantiate and cache config based on the environment."""
    env_state = env_state or BaseConfig().ENV_STATE or "dev"

    config_classes: dict[str, Type[GlobalConfig]] = {
        "dev": DevConfig,
        "prod": ProdConfig,
        "test": TestConfig,
    }

    try:
        # logger.debug(config_classes)
        logger.debug(ROOT)
        return config_classes[env_state.lower()]()
    except KeyError:
        raise ValueError(f"Unknown environment state: {env_state}")


config = get_config()
