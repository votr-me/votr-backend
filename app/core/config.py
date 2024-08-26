import pathlib
from functools import lru_cache
from typing import Optional, Type, Union, ClassVar

from pydantic_settings import BaseSettings

# Define the root directory
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


class BaseConfig(BaseSettings):
    APP_NAME: str = "Votr"
    PROJECT_VERSION: str = "0.0.0"
    ENV_STATE: Optional[str] = None
    PROJECT_DESCRIPTION: Optional[str] = None
    api_v1_str: str = "/api/v1"
    GEOCODIO_BASE_URL: ClassVar[str] = "https://api.geocod.io/v1.7/"
    CACHE_TTL: Optional[int] = 3600

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
    sting: bool = True

    DATABASE_URL: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    GEOCODIO_API_KEY: Optional[str] = None
    CONGRESS_GOV_API_KEY: Optional[str] = None
    OPENSECRETS_API_KEY: Optional[str] = None
    CACHE_TTL: Optional[int] = None
    REDIS_URL: Optional[str] = None
    FEC_API_KEY: Optional[str] = None
    DEV_USER_SESSION_KEY: Optional[str] = None
    DEV_DBLOGS: Optional[bool] = None

    class Config:
        env_prefix = "DEV_"


class ProdConfig(GlobalConfig):
    LOG_LVL: str = "INFO"
    testing: bool = False
    PROD_DBLOGS: Optional[bool] = None

    class Config:
        env_prefix = "PROD_"


class TestConfig(GlobalConfig):
    LOG_LVL: str = "TEST"
    testing: bool = True
    TEST_DBLOGS: Optional[bool] = None

    class Config:
        env_prefix = "TEST_"


@lru_cache()
def get_config(
    env_state: Optional[str] = None,
) -> Union[DevConfig, ProdConfig, TestConfig]:
    """Instantiate and cache config based on the environment."""
    if env_state is None:
        env_state = BaseConfig().ENV_STATE or "dev"

    config_classes: dict[str, Type[GlobalConfig]] = {
        "dev": DevConfig,
        "prod": ProdConfig,
        "test": TestConfig,
    }

    config_class = config_classes.get(env_state.lower())
    if not config_class:
        raise ValueError(f"Unknown environment state: {env_state}")

    return config_class()


config = get_config()
