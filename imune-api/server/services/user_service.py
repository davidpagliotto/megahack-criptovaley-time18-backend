from server.models.user_model import User, UserOutput
from server.repositories.user_repository import UserRepository
from server.services.base_service import BaseService
from server.services.firebase_service import FirebaseService


class UserService(BaseService):

    def __init__(self):
        super().__init__(UserRepository())

    async def upsert(self, user: User, attr=None, value=None):
        fb_service = FirebaseService()
        fb_user = await fb_service.create_user(user)
        if fb_user:
            user.uid = fb_user.get('localId')
            await super(UserService, self).upsert(user, 'email', user.email)
            return UserOutput.parse_obj(user.dict())
