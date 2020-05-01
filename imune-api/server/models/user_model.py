from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str
    password: str


class UserSchema(BaseModel):
    uid: str
    email: str
    name: str
    password: str


class User:
    uid: str
    email: str
    name: str
    password: str
