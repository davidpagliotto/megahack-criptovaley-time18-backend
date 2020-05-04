from uuid import UUID

from server.models.base_model import ApiBaseModel


class Occurrence(ApiBaseModel):
    address: str
    batch: UUID
    document: str
    document_type: str
    vaccine: str
    death: bool
    effects: str
    geo: str = None
