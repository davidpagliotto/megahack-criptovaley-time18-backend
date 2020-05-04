from datetime import datetime
from enum import Enum
from uuid import UUID

from server.models.base_model import ApiBaseModel
from server.models.vaccine_model import Vaccine


class DocumentType(str, Enum):
    CPF = 'cpf'
    RG = 'RG'
    CNH = 'CNH'
    PASSPORT = 'passport'
    OTHER = 'other'


class Vaccinate(ApiBaseModel):
    name: str
    responsible: UUID
    batch: UUID
    document_type: DocumentType
    document: str
    date_of_vaccination: datetime
    vaccine: UUID
    transaction_id: str


class VaccinateOutput(Vaccinate):
    vaccine_obj: Vaccine
