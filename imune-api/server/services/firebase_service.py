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
            await self._handler_error(e)
        except Exception as e:
            raise LoginException(status_code=400, message='Error on get token')

    def validate_token(self, id_token):
        try:
            info = self.auth.get_account_info(id_token)
            users = info.get('users')
            if len(users) > 0:
                email_verified = users[0].get('emailVerified')
                if not email_verified:
                    raise LoginException(message='Email not verified')
            return True
        except LoginException as e:
            raise e
        except Exception as e:
            return False

        return False

    async def create_user(self, user: User):
        try:
            fb_user = self.auth.create_user_with_email_and_password(user.email, user.password)
            self.auth.send_email_verification(fb_user.get('idToken'))
            return fb_user
        except HTTPError as e:
            await self._handler_error(e)
        except Exception as e:
            raise LoginException(status_code=400, message='Error on create user')

    @staticmethod
    async def _handler_error(error):
        if 'INVALID_EMAIL' in error.strerror:
            raise LoginException(status_code=401, message='Invalid email')
        if 'INVALID_PASSWORD' in error.strerror:
            raise LoginException(status_code=401, message='Invalid password')
        if 'TOO_MANY_ATTEMPTS_TRY_LATER' in error.strerror:
            raise LoginException(status_code=400, message='Too many attempts')
        if 'WEAK_PASSWORD' in error.strerror:
            raise LoginException(status_code=400, message='Password too weak. Should be at least 6 characters')
        if 'EMAIL_EXISTS' in error.strerror:
            raise LoginException(status_code=400, message='Email already exists')
        else:
            raise LoginException(status_code=400, message=error.strerror)
