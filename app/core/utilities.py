import datetime
import hashlib
import logging
from typing import Any, Callable, Dict

from fastapi import HTTPException, Query, Request

from app.core.logging_config import configure_logging
from .constants import US_STATE_ABBREVIATIONS

configure_logging()
from app.core.logging_config import configure_logging


configure_logging()
logger = logging.getLogger("app")


def clean_legislator_data(legislator: Dict[str, Any]) -> Dict[str, Any]:
    for key, value in legislator.items():
        if value == "" or value == " ":
            legislator[key] = None

    if "birthdate" in legislator and legislator["birthdate"]:
        try:
            legislator["birthdate"] = datetime.datetime.strptime(
                str(legislator["birthdate"]), "%Y-%m-%d"
            ).date()
        except ValueError:
            legislator["birthdate"] = None

    return legislator


def validate_state_id(state_id: str) -> str:
    if state_id.upper() not in US_STATE_ABBREVIATIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid state ID, {state_id} is not a valid state ID",
        )
    return state_id.upper()


def date_converter(o):
    if isinstance(o, datetime.date):
        return o.isoformat()
    raise TypeError("Type not serializable")


def parse_geocodio_fields(fields: str = Query(None, fields="Data fields to return")):
    if fields:
        return [field.strip() for field in fields.split(",")]
    else:
        return []


def generate_param_hash(params: Dict) -> str:
    sorted_params = sorted(params.items())
    param_str = "|".join(f"{k}:{v}" for k, v in sorted_params)
    hashed_part = hashlib.md5(param_str.encode("utf-8")).hexdigest()
    return hashed_part


def custom_cache_key_generator(
    prefix: str,
    namespace: str,
    identifier: str,
    param_hash: str,
    max_key_length: int = 200,
) -> str:
    key_parts = [prefix, namespace, identifier, param_hash]
    full_key = ":".join(str(part) for part in key_parts if part)

    if len(full_key) > max_key_length:
        full_key = hashlib.md5(full_key.encode("utf-8")).hexdigest()
    return full_key


def generic_cache_key_builder(func: Callable, *args, **kwargs) -> str:
    request: Request = kwargs["request"]
    query_params = dict(request.query_params)

    prefix = "votr"
    namespace = request.url.path.replace("/", ":").strip(":")
    identifier = query_params.get(
        "bioguideId", ""
    )  # Change 'id' to the appropriate identifier if necessary
    param_hash = generate_param_hash(query_params)

    key = custom_cache_key_generator(
        prefix=prefix, namespace=namespace, identifier=identifier, param_hash=param_hash
    )
    return key
