import logging
import os
from datetime import datetime
from logging.config import dictConfig

from app.core.config import DevConfig, config
from .security.APIKeyLoggerRedactor import RedactApiKeyFilter


def configure_logging() -> None:
    log_dir = config.logs_directory
    log_file_name = f'votr_logs_{datetime.now().strftime("%Y-%m-%d")}.log'
    log_file_path = os.path.join(log_dir, log_file_name)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Create the logs directory if it doesn't exist

    handlers = ["default", "timed_rotating_file"]

    api_keys_to_redact = [
        config.OPENSECRETS_API_KEY,
        config.GEOCODIO_API_KEY,
        config.FEC_API_KEY,
        config.CONGRESS_GOV_API_KEY,
    ]

    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "correlation_id": {
                    "()": "asgi_correlation_id.CorrelationIdFilter",
                    "uuid_length": 8 if isinstance(config, DevConfig) else 32,
                    "default_value": "-",
                },
                "redact_api_key": {
                    "()": RedactApiKeyFilter,
                    "api_keys": api_keys_to_redact,
                },
            },
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(asctime)s %(msecs)03d %(levelname)s %(name)s %(lineno)d %(message)s",
                },
                "file": {
                    "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(asctime)s %(msecs)03d %(levelname)s %(correlation_id)s %(name)s %(lineno)d %(message)s",
                },
                "web": {
                    "class": "logging.Formatter",
                    "datefmt": "%H:%M:%S",
                    "format": "%(asctime)s %(msecs)03d %(levelname)s [%(correlation_id)s] %(name)s %(lineno)d %(message)s",
                },
            },
            "handlers": {
                "default": {
                    "class": "rich.logging.RichHandler",
                    "level": "DEBUG",
                    "formatter": "console",
                    "filters": ["redact_api_key"],
                },
                "timed_rotating_file": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "file",
                    "filters": ["correlation_id", "redact_api_key"],
                    "filename": log_file_path,
                    "when": "midnight",
                    "interval": 1,
                    "backupCount": 7,
                    "encoding": "utf8",
                },
            },
            "loggers": {
                "uvicorn": {
                    "handlers": ["default", "timed_rotating_file"],
                    "level": "INFO",
                    "propagate": True,
                },
                "fastapi": {
                    "handlers": handlers,
                    "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                    "propagate": False,
                },
                "app": {
                    "handlers": handlers,
                    "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                    "propagate": True,
                },
                "sqlalchemy.engine": {
                    "handlers": handlers,
                    "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                    "propagate": False,
                },
                "sqlalchemy.pool": {
                    "handlers": handlers,
                    "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                    "propagate": False,
                },
                "graphql": {  # New logger for GraphQL
                    "handlers": handlers,
                    "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                    "propagate": True,
                },
            },
        }
    )


# Ensure the root logger does not duplicate logs
logging.getLogger().handlers.clear()
