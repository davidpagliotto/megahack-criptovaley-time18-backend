from typing import List
from uuid import UUID

from server.models.base_model import ApiBaseModel


class Item(ApiBaseModel):
    vaccine_guid: UUID
    quantity: float
    supplier: str
    enable: bool = True
    quantity: float
    item_address: str
    item_guid: UUID


class Batch(ApiBaseModel):
    address: str = None
    supplier: UUID  # Guid person
    batch_origin: str = None
    document_number: str
    document: str  # s3 path
    geo: str = None
    responsible: UUID  # Guid person
    items: List[Item]
