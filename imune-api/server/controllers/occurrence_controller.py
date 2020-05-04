from typing import List

from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.occurrence_model import Occurrence
from server.services.occurrence_service import OccurrenceService

router = APIRouter()
occurrence_router = {
    "router": router,
    "prefix": "/occurrence",
    "tags": ["Occurrence"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="", response_model=Occurrence)
async def post(occurrence: Occurrence):
    occurrence_service = OccurrenceService()
    return await occurrence_service.upsert(occurrence)


@router.get(path="", response_model=List[Occurrence])
async def get_all():
    occurrence_service = OccurrenceService()
    return await occurrence_service.get_all()


@router.get(path="/{guid}", response_model=Occurrence)
async def get_by_guid(guid):
    occurrence_service = OccurrenceService()
    return await occurrence_service.get_by_guid(guid)
