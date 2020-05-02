from server.models.batch_model import Batch
from server.repositories.batch_repository import BatchRepository
from server.services.base_service import BaseService


class BatchService(BaseService):

    def __init__(self):
        super().__init__(BatchRepository())

    async def upsert(self, batch: Batch, attr=None, value=None):
        # TODO validar vinculos.
        return await super().upsert(batch)
