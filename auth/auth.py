import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name = "X-API-KEY")

def get_api_key(api_key: str = Security(API_KEY_HEADER)) -> str:
    expected_key = os.getenv("API_KEY")
    if api_key != expected_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail = "Invalid or missing API key"
        )
    return api_key

