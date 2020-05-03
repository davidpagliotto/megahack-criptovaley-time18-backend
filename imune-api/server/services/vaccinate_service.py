from server.exception.exception import NotFoundException, BusinessValidationException
from server.models.vaccinate_model import Vaccinate
from server.repositories.vaccinate_repository import VaccinateRepository
from server.services.base_service import BaseService
from server.services.batch_service import BatchService
from server.services.person_service import PersonService
from server.services.vaccine_service import VaccineService


class VaccinateService(BaseService):

    def __init__(self):
        super().__init__(VaccinateRepository())
        self._person_service = PersonService()
        self._batch_service = BatchService()
        self._vaccine_service = VaccineService()

    async def upsert(self, vaccinate: Vaccinate, attr=None, value=None):
        await self._validate_vaccinate(vaccinate)
        return await super().upsert(vaccinate, attr, value)

    async def _validate_vaccinate(self, vaccinate: Vaccinate):

        try:
            await self._person_service.get_by_guid(vaccinate.responsible)
        except NotFoundException:
            raise BusinessValidationException('Invalid Responsible')

        try:
            await self._batch_service.get_by_guid(vaccinate.batch)
        except NotFoundException:
            raise BusinessValidationException('Invalid Batch')

        try:
            await self._vaccine_service.get_by_guid(vaccinate.vaccine)
        except NotFoundException:
            raise BusinessValidationException('Invalid Vaccine')
