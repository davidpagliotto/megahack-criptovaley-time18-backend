from requests import HTTPError

from server.exception.exception import LoginException
from server.firebase import firebase
from server.models.user_model import User


class FirebaseService:

    def __init__(self):
        self.auth = firebase.init_firebase_app().auth()

    async def token(self, email: str, password: str):
        try:
            fb_user = self.auth.sign_in_with_email_and_password(email, password)
            if fb_user:
                return fb_user.get('idToken')
        except HTTPError as e:
            if 'INVALID_EMAIL' in e.strerror:
                raise LoginException(message='Invalid email')
            if 'INVALID_PASSWORD' in e.strerror:
                raise LoginException(message='Invalid password')
            if 'TOO_MANY_ATTEMPTS_TRY_LATER' in e.strerror:
                raise LoginException(message='Too many attempts')
            else:
                raise LoginException(message=e.strerror)

    def validate_token(self, id_token):
        try:
            info = self.auth.get_account_info(id_token)
            print(info.get('users'))
            return True
        except Exception as e:
            print(e)
            return False

    async def create_user(self, user: User):
        try:
            fb_user = self.auth.create_user_with_email_and_password(user.email, user.password)
            return fb_user
        except Exception as e:
            raise LoginException(status_code=400, message='Error on create user')

    @staticmethod
    async def update_user(user: User):
        pass
        # params = dict(
        #     email=user.email,
        #     password=user.password,
        #     display_name=user.name,
        #     disabled=False
        # )
        # fb_user = fb_auth.update_user(user.uid, **params)
        # print(fb_user)
