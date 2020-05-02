from server.enums.enums import Collections
from server.models.vaccine_model import Vaccine
from server.repositories.base_repository import BaseRepository


class VaccineRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.VACCINES.value, Vaccine)
