from server.enums.enums import Collections
from server.models.batch_model import BatchTransaction
from server.repositories.base_repository import BaseRepository


class BatchTransactionRepository(BaseRepository):

    def __init__(self):
        super().__init__(Collections.BATCH_TRANSACTIONS.value, BatchTransaction)
