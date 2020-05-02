from uuid import UUID

from server.models.base_model import ApiBaseModel


class Batch(ApiBaseModel):
    address: str = None
    fornecedor: UUID  # Guid person
    batch_origin: str = None
    nf: str
    document: str  # s3 path
    geo: str = None
    responsible: UUID  # Guid person


class BatchItem(ApiBaseModel):
    quantity: float
    batch_address: str
    batch_guid: UUID
    item_address: str
    item_guid: UUID


class Item(ApiBaseModel):
    vaccine_guid: UUID
    quantity: float
    supplier: str
    enable: bool = True
