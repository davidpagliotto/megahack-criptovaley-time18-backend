from server.enums.enums import Collections
from server.models.occurrence_model import Occurrence
from server.repositories.base_repository import BaseRepository


class OccurrenceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.OCCURRENCES.value, Occurrence)
