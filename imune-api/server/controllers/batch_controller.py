from typing import List

from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.batch_model import Batch
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


@router.get(path="", response_model=List[Batch])
async def get_all():
    batch_service = BatchService()
    return await batch_service.get_all()


@router.get(path="/{guid}", response_model=Batch)
async def get_by_guid(guid):
    batch_service = BatchService()
    return await batch_service.get_by_guid(guid)
