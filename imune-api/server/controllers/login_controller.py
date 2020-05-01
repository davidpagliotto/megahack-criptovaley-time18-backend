from fastapi import APIRouter

from server.models.user_model import LoginSchema

router = APIRouter()
login_router = {
    "router": router,
    "prefix": "/login",
    "tags": ["Login"],
}


@router.post(path="")
def post_login(login: LoginSchema):
    return 'OK'
