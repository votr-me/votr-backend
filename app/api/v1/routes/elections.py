import logging

from fastapi import APIRouter

from app.core.logging_config import configure_logging

router = APIRouter()

configure_logging()
logger = logging.getLogger(__name__)
