from uuid import UUID

from server.models.base_model import ApiBaseModel
from server.models.vaccinate_model import DocumentType


class Occurrence(ApiBaseModel):
    address: str
    batch: UUID
    document: str
    document_type: DocumentType
    vaccine: str
    death: bool
    effects: str
