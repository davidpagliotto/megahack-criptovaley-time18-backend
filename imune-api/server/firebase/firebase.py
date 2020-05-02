from pyrebase import pyrebase

from server.configurations.environment import env


def init_firebase_app():
    return pyrebase.initialize_app(env.firebase_conf())
