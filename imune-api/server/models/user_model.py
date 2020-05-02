from pydantic import BaseModel

from server.models.base_model import ApiBaseModel


class User(ApiBaseModel):
    uid: str = None
    email: str = None
    name: str = None
    password: str = None


class Login(BaseModel):
    email: str
    password: str


class UserOutput(BaseModel):
    uid: str = None
    email: str = None
    name: str = None
    token: str = None


