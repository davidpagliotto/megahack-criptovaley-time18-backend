from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.vacina_model import Vaccine
from server.services.vaccine_service import VaccineService

router = APIRouter()
vaccine_router = {
    "router": router,
    "prefix": "/vaccine",
    "tags": ["Vaccine"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="")
async def post_vaccine(vaccine: Vaccine):
    return await VaccineService.index_vaccine(vaccine)
