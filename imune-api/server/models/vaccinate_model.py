from datetime import datetime
from enum import Enum
from uuid import UUID

from server.models.base_model import ApiBaseModel


class DocumentType(str, Enum):
    CPF = 'cpf'
    RG = 'RG'
    CNH = 'CNH'
    PASSPORT = 'passport'
    OTHER = 'other'


class Vaccinate(ApiBaseModel):
    nome: str
    responsible: UUID
    batch: UUID
    document_type: DocumentType
    document: str
    date_of_vaccination: datetime
    vaccine: UUID
