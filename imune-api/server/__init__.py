import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials
from starlette.middleware.cors import CORSMiddleware

from server.controllers.login_controller import login_router
from server.controllers.user_controller import user_router


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

    app.include_router(
        **user_router,
    )
    app.include_router(
        **login_router
    )

    _init_firebase_app()
    return app


def _init_firebase_app():
    cred = credentials.Certificate("imune-service-account-key.json")
    firebase_admin.initialize_app(cred)
