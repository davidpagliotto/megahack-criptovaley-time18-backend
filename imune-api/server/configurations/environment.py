import json
import os

from server.exception.exception import EnvironmentException


class Environment:
    def __init__(self):
        self.ENV_API_HOST: str = os.getenv("ENV_API_HOST")
        self.ENV_API_PORT: str = os.getenv("ENV_API_PORT")
        self.ENV_DATABASE_URL: str = os.getenv("ENV_DATABASE_URL")
        self.ENV_DATABASE_NAME: str = os.getenv("ENV_DATABASE_NAME")
        self.ENV_FIREBASE_CONF: str = os.getenv("ENV_FIREBASE_CONF")

        self.valida_environment()

    def valida_environment(self):
        msg = ""
        if self.ENV_API_HOST is None:
            msg = "ENV_API_HOST not configured "
        if self.ENV_API_PORT is None:
            msg += "ENV_API_PORT not configured "
        if self.ENV_DATABASE_URL is None:
            msg += "ENV_DATABASE_URL not configured "

        try:
            json.loads(self.ENV_FIREBASE_CONF)
        except Exception as e:
            msg += "Error to load firebase confs "

        if len(msg) > 0:
            raise EnvironmentException(msg)

    def api_host(self) -> str:
        return self.ENV_API_HOST

    def api_port(self) -> int:
        return int(self.ENV_API_PORT)

    def database_url(self) -> str:
        return self.ENV_DATABASE_URL

    def database_name(self) -> str:
        return self.ENV_DATABASE_NAME

    def firebase_conf(self) -> str:
        return json.loads(self.ENV_FIREBASE_CONF)


env = Environment()
