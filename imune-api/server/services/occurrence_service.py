from server.exception.exception import NotFoundException, BusinessValidationException
from server.models.occurrence_model import Occurrence
from server.repositories.occurrence_repository import OccurrenceRepository
from server.services.base_service import BaseService
from server.services.batch_service import BatchService


class OccurrenceService(BaseService):

    def __init__(self):
        super().__init__(OccurrenceRepository())
        self._batch_service = BatchService()

    async def upsert(self, occurrence: Occurrence, attr=None, value=None):
        await self._validate_occurrence(occurrence)
        return await super().upsert(occurrence, attr, value)

    async def _validate_occurrence(self, occurrence):
        try:
            await self._batch_service.get_by_guid(occurrence.guid)
        except NotFoundException:
            raise BusinessValidationException('Invalid Batch')
