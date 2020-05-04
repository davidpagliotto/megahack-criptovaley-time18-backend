from server.enums.enums import Collections
from server.models.vaccinate_model import Vaccinate, VaccinateOutput
from server.repositories.base_repository import BaseRepository
from server.services.vaccine_service import VaccineService


class VaccinateRepository(BaseRepository):

    def __init__(self):
        super().__init__(Collections.VACCINATES.value, Vaccinate)

    async def get_all(self, parameters: dict = None):
        vaccinates = await super(VaccinateRepository, self).get_all(parameters)

        vaccine_guids = list(map(lambda e: e.vaccine, vaccinates))
        vaccines_service = VaccineService()
        vaccines = await vaccines_service.get_many_by_guids(vaccine_guids)

        ret = []
        for vaccinate in vaccinates:
            d = vaccinate.dict()
            d['vaccine_name'] = list(map(lambda e: e.name, vaccines))[0]
            ret.append(VaccinateOutput(**d))

        return ret
