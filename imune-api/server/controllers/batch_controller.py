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
