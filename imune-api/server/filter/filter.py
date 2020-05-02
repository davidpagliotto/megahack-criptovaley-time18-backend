from fastapi import HTTPException
from fastapi.params import Security
from fastapi.security import APIKeyHeader

from server.exception.exception import LoginException
from server.services.firebase_service import FirebaseService

x_api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_token(api_key_header: str = Security(x_api_key_header)):
    if not api_key_header:
        raise HTTPException(status_code=401, detail="token header invalid")

    fb_service = FirebaseService()
    if not fb_service.validate_token(api_key_header):
        raise LoginException(message='Invalid token')

    print('Token ok')
