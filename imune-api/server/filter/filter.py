from fastapi import HTTPException
from fastapi.params import Security
from fastapi.security import APIKeyHeader

x_api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_token(api_key_header: str = Security(x_api_key_header)):
    if api_key_header != "1":
        raise HTTPException(status_code=404, detail="token header invalid")
