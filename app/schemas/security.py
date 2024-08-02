from pydantic import BaseModel


class APIKeyCreate(BaseModel):
    key_hash: str
    salt: str


class APIKey(APIKeyCreate):
    key_hash: str
    salt: str
