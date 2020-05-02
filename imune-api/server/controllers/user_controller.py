from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.user_model import User
from server.services.user_service import UserService

router = APIRouter()
user_router = {
    "router": router,
    "prefix": "/users",
    "tags": ["User"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="")
async def post_user(user: User):
    user_service = UserService()
    return await user_service.upsert(user)
