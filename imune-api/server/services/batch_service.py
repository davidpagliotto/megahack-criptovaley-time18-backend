from typing import List
from uuid import UUID

from server.exception.exception import NotFoundException, BusinessValidationException
from server.models.batch_model import Batch, BatchTransaction
from server.models.person_model import Person
from server.models.vaccine_model import Vaccine
from server.repositories.batch_repository import BatchRepository
from server.repositories.batch_transaction_repository import BatchTransactionRepository
from server.services.base_service import BaseService
from server.services.person_service import PersonService
from server.services.vaccine_service import VaccineService


class BatchService(BaseService):

    def __init__(self):
        super().__init__(BatchRepository())
        self._person_service = PersonService()
        self._vaccine_service = VaccineService()

    async def upsert(self, batch: Batch, attr=None, value=None):
        await self._validate_batch(batch)
        batch = await super().upsert(batch)

        await self._first_transaction(batch)

        return batch

    async def _validate_batch(self, batch):
        if not batch.items or len(batch.items) == 0:
            raise BusinessValidationException('Is not possible register a batch without itens')

        vaccines_guids_request = [i.vaccine_guid for i in batch.items]
        vaccines_guids_request_set = set(vaccines_guids_request)
        vaccines: List[Vaccine] = await self._vaccine_service.get_many_by_guids(vaccines_guids_request)
        vaccines_guids_response = [v.guid for v in vaccines]
        vaccines_guids_response_set = set(vaccines_guids_response)

        if len(vaccines_guids_response_set) != len(vaccines_guids_request_set):
            raise BusinessValidationException(
                f'Some vaccines were not found on database. {vaccines_guids_request_set - vaccines_guids_response_set}')

        suppliers_guids_request = [i.supplier for i in batch.items]
        suppliers_guids_request_set = set(suppliers_guids_request)
        suppliers: List[Person] = await self._person_service.get_many_by_guids(suppliers_guids_request)
        suppliers_guids_response = [s.guid for s in suppliers]
        suppliers_guids_response_set = set(suppliers_guids_response)

        if len(suppliers_guids_response_set) != len(suppliers_guids_request_set):
            raise BusinessValidationException(f'Some suppliers were not found on database. '
                                              f'{suppliers_guids_request_set - suppliers_guids_response_set}')
        try:
            await self._person_service.get_by_guid(batch.supplier)
        except NotFoundException:
            raise BusinessValidationException('Invalid Supplier')

        try:
            await self._person_service.get_by_guid(batch.responsible)
        except NotFoundException:
            raise BusinessValidationException('Invalid Responsible')

        if batch.batch_origin:
            try:
                await self._repository.get_by_guid(batch.batch_origin)
            except NotFoundException:
                raise BusinessValidationException('Invalid Batch Origin')

    async def _first_transaction(self, batch: Batch):
        transaction = BatchTransaction(
            batch=batch.guid,
            description='Initial transaction',
            responsible=batch.responsible,
            geo=batch.geo,
            destiny='Storage',
            transaction_id=batch.transaction_id)

        await self.create_transaction(batch.guid, transaction)

    async def get_transactions(self, batch_guid: UUID):
        try:
            await self._repository.get_by_guid(batch_guid)
        except NotFoundException:
            raise BusinessValidationException('Invalid Batch')

        repository = BatchTransactionRepository()
        return await repository.get_all({"batch": str(batch_guid)})

    async def create_transaction(self, batch_guid: UUID, transaction: BatchTransaction):
        await self._validate_transaction(batch_guid, transaction)

        repository = BatchTransactionRepository()
        return await repository.upsert(transaction)

    async def _validate_transaction(self, batch_guid: UUID, transaction: BatchTransaction):
        if not transaction.description.strip():
            raise BusinessValidationException('Description must be informed in Transaction')

        if not transaction.destiny.strip():
            raise BusinessValidationException('Destiny must be informed in Transaction')

        try:
            await self._repository.get_by_guid(batch_guid)
        except NotFoundException:
            raise BusinessValidationException('Invalid Batch into Transaction')

        try:
            await self._person_service.get_by_guid(transaction.responsible)
        except NotFoundException:
            raise BusinessValidationException('Invalid Responsible into Transaction')