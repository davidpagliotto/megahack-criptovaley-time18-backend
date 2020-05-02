from uuid import UUID

from pydantic import BaseModel


class ApiBaseModel(BaseModel):
    guid: UUID = None

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)

        for key in d.keys():
            value = d[key]
            if type(value) == UUID:
                d[key] = str(value)

        return d
