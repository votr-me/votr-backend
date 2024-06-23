from typing import Dict, Any
from fastapi import HTTPException, Query
from .constants import US_STATE_ABBREVIATIONS
import datetime


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
