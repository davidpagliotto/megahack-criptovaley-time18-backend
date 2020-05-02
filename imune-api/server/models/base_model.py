from uuid import UUID

from pydantic import BaseModel


class ApiBaseModel(BaseModel):
    guid: UUID = None
