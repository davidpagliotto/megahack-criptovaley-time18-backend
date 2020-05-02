from typing import List

from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.vaccine_model import Vaccine
from server.services.vaccine_service import VaccineService

router = APIRouter()
vaccine_router = {
    "router": router,
    "prefix": "/vaccine",
    "tags": ["Vaccine"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="", response_model=Vaccine)
async def post(vaccine: Vaccine):
    vaccine_service = VaccineService()
    return await vaccine_service.upsert(vaccine)


@router.get(path="", response_model=List[Vaccine])
async def get_all():
    vaccine_service = VaccineService()
    return await vaccine_service.get_all()


@router.get(path="/{guid}", response_model=Vaccine)
async def get_by_guid(guid):
    vaccine_service = VaccineService()
    return await vaccine_service.get_by_guid(guid)
