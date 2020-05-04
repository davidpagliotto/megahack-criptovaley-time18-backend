from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.vaccinate_model import Vaccinate, VaccinateOutput
from server.services.vaccinate_service import VaccinateService

router = APIRouter()
vaccinate_router = {
    "router": router,
    "prefix": "/vaccinate",
    "tags": ["Vaccinate"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="", response_model=Vaccinate)
async def post(vaccinate: Vaccinate):
    vaccinate_service = VaccinateService()
    return await vaccinate_service.upsert(vaccinate)


@router.get(path="", response_model=List[VaccinateOutput])
async def get_all(document: str = None, batch: UUID = None, vaccine: UUID = None, responsible: UUID = None):
    parameters = {
        'document': document,
        'batch': batch,
        'vaccine': vaccine,
        'responsible': responsible
    }
    vaccinate_service = VaccinateService()
    return await vaccinate_service.get_all(parameters)


@router.get(path="/{guid}", response_model=Vaccinate)
async def get_by_guid(guid):
    vaccinate_service = VaccinateService()
    return await vaccinate_service.get_by_guid(guid)
