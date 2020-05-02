from pydantic import BaseModel


class ApiBaseModel(BaseModel):
    guid: str = None
