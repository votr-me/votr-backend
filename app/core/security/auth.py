from typing import Dict

# from argon2 import PasswordHasher
import argon2
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from app.schemas.security.security import APIKeyCreate
import secrets
import os

import logging
from app.core.logging_config import configure_logging

configure_logging()
from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")

ph = argon2.PasswordHasher()
api_key_header = APIKeyHeader(name="X-API-Key")
VALID_API_KEYS: Dict[str, APIKeyCreate] = {}


def hash_api_key(api_key: str) -> APIKeyCreate:
    """Hash an API key and return the hash and salt."""
    salt = os.urandom(16)  # Generate 16 random bytes as the salt
    hash = ph.hash(api_key + salt.hex())
    return APIKeyCreate(key_hash=hash, salt=salt.hex())


def verify_api_key(hashed_key: str, salt: str, api_key: str) -> bool:
    try:
        ph.verify(hashed_key, api_key + salt)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False


def generate_api_key(length: int = 32) -> str:
    """Generate a cryptographically secure API key of the specified length."""
    return secrets.token_urlsafe(length)


async def get_api_key(api_key: str = Security(api_key_header)):
    for key, key_data in VALID_API_KEYS.items():
        if verify_api_key(key_data.key_hash, key_data.salt, api_key):
            return key
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key"
    )
