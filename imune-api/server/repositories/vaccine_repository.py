from typing import TypeVar

from server.enums.enums import Collections
from server.repositories.base_repository import BaseRepository

T = TypeVar('T')


class VaccineRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.VACCINES.value)
