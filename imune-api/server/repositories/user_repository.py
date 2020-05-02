from server.enums.enums import Collections
from server.models.user_model import User
from server.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(Collections.USERS.value, User)
