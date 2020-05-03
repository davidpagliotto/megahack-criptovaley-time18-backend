from typing import List
from uuid import UUID

from server.models.base_model import ApiBaseModel


class Item(ApiBaseModel):
    vaccine_guid: UUID
    quantity: float
    supplier: UUID
    enable: bool = True
    quantity: float
    address: str = None


class Batch(ApiBaseModel):
    address: str = None
    supplier: UUID  # Guid person
    batch_origin: UUID = None  # Guid batch origem
    document_number: str
    document: str = None  # s3 path
    document_type: str = None
    geo: str = None
    responsible: UUID  # Guid person
    items: List[Item]
    transaction_id: str


class BatchTransaction(ApiBaseModel):
    address: str = None
    batch: UUID  # Guid person
    destiny: str
    description: str
    geo: str = None
    responsible: UUID  # Guid person
    transaction_id: str
