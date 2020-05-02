from typing import List
from uuid import UUID

from server.models.base_model import ApiBaseModel


class Item(ApiBaseModel):
    vaccine_guid: UUID
    quantity: float
    supplier: UUID
    enable: bool = True
    quantity: float
    address: str


class Batch(ApiBaseModel):
    address: str = None
    supplier: UUID  # Guid person
    batch_origin: UUID = None  # Guid batch origem
    document_number: str
    document: str  # s3 path
    geo: str = None
    responsible: UUID  # Guid person
    items: List[Item]
