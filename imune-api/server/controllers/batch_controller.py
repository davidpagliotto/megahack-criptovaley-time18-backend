from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.batch_model import Batch, BatchTransaction
from server.services.batch_service import BatchService

router = APIRouter()
batch_router = {
    "router": router,
    "prefix": "/batch",
    "tags": ["Batch"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="", response_model=Batch)
async def post(batch: Batch):
    batch_service = BatchService()
    return await batch_service.upsert(batch)


@router.get(path="/{batch_guid}/transactions", response_model=List[BatchTransaction])
async def get_transaction(batch_guid: UUID):
    batch_service = BatchService()
    return await batch_service.get_transactions(batch_guid)


@router.post(path="/{batch_guid}/transactions", response_model=BatchTransaction)
async def post_transaction(batch_guid: UUID, transaction: BatchTransaction):
    batch_service = BatchService()
    return await batch_service.create_transaction(batch_guid, transaction)
