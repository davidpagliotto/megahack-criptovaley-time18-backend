from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.user_model import UserSchema

router = APIRouter()
user_router = {
    "router": router,
    "prefix": "/users",
    "tags": ["User"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="")
def post_user(user: UserSchema):
    return 'OK'
