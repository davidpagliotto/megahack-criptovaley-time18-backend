from typing import List

from fastapi import APIRouter, Depends

from server.filter.filter import get_token
from server.models.person_model import Person
from server.services.person_service import PersonService

router = APIRouter()
person_router = {
    "router": router,
    "prefix": "/person",
    "tags": ["Person"],
    "dependencies": [Depends(get_token)]
}


@router.post(path="", response_model=Person)
async def post(person: Person):
    person_service = PersonService()
    return await person_service.upsert(person)


@router.get(path="", response_model=List[Person])
async def get_all(document: str = None, full_name: str = None):
    parameters = {
        'document': document,
        'full_name': full_name
    }
    person_service = PersonService()
    return await person_service.get_all(parameters)


@router.get(path="/{guid}", response_model=Person)
async def get_by_guid(guid):
    person_service = PersonService()
    return await person_service.get_by_guid(guid)
