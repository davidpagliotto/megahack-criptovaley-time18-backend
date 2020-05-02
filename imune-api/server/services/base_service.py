from server.database.database import db
from server.models.base_model import ApiBaseModel


class BaseService:

    def __init__(self, repository):
        self.db = db
        self._repository = repository

    async def upsert(self, model: ApiBaseModel):
        return await self._repository.upsert(model)

    async def get_all(self, parameters=None):
        return await self._repository.get_all(parameters)

    async def get_by_guid(self, guid):
        return await self._repository.get_by_guid(guid)
