from server.repositories.vaccine_repository import VaccineRepository
from server.services.base_service import BaseService


class VaccineService(BaseService):

    def __init__(self):
        super().__init__(VaccineRepository())
