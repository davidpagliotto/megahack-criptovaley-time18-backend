from server.models.user_model import UserOutput
from server.services.firebase_service import FirebaseService
from server.services.user_service import UserService


class LoginService:

    @staticmethod
    async def login(email, password):
        fb_service = FirebaseService()
        token = await fb_service.token(email, password)

        user_service = UserService()
        user = await user_service.get_one_by_attr_value('email', email)

        params = user.dict()
        params['token'] = token
        return UserOutput.parse_obj(params)
