import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials
from starlette.middleware.cors import CORSMiddleware

from server.controllers.login_controller import login_router
from server.controllers.user_controller import user_router
from server.controllers.vaccine_controller import vaccine_router
from server.database.database import connect_to_mongo, close_mongo_connection


def init_app() -> FastAPI:
    app = FastAPI(
        title="Imune",
        description="Imune API",
        version="0.0.1",
        redoc_url=None,
    )

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    routers = [user_router, login_router, vaccine_router]

    [app.include_router(**r) for r in routers]

    _init_firebase_app()

    app.add_event_handler("startup", connect_to_mongo)
    app.add_event_handler("shutdown", close_mongo_connection)

    return app


def _init_firebase_app():
    cred = credentials.Certificate("imune-service-account-key.json")
    firebase_admin.initialize_app(cred)
