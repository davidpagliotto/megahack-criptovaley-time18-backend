from server.enums.enums import Collections
from server.models.person_model import Person
from server.repositories.base_repository import BaseRepository


class PersonRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.PEOPLE.value, Person)
