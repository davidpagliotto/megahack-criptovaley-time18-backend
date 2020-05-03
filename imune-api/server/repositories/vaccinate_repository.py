from server.enums.enums import Collections
from server.models.vaccinate_model import Vaccinate
from server.repositories.base_repository import BaseRepository


class VaccinateRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.VACCINATES.value, Vaccinate)
