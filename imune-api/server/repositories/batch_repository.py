from server.enums.enums import Collections
from server.models.batch_model import Batch
from server.repositories.base_repository import BaseRepository


class BatchRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.BATCHES.value, Batch)
