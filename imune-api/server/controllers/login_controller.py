from fastapi import APIRouter

from server.models.user_model import Login, UserOutput
from server.services.login_service import LoginService

router = APIRouter()
login_router = {
    "router": router,
    "prefix": "/login",
    "tags": ["Login"],
}


@router.post(path="", response_model=UserOutput)
async def post_login(login: Login):
    login_service = LoginService()
    return await login_service.login(login.email, login.password)
