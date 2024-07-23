from app.core.dependencies import get_geocodio_client
from app.core.logging_config import configure_logging
from app.services import GeocodioAsyncAPIClient
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi_cache.decorator import cache
from fastapi_limiter.depends import RateLimiter
from typing import List, Optional, Union, Any, Dict
import httpx
import logging

router = APIRouter()

configure_logging()
logger = logging.getLogger(__name__)
