from pydantic import BaseModel


class Vaccine(BaseModel):
    guid: str = None
    nome: str
