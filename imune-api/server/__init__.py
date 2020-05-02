from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.controllers.login_controller import login_router
from server.controllers.person_controller import person_router
from server.controllers.user_controller import user_router
from server.controllers.vaccine_controller import vaccine_router
from server.database.database import connect_to_mongo, close_mongo_connection, apply_migrations
from server.exception.exception import ApiBaseException, EnvironmentException, LoginException, \
    BusinessValidationException, generic_render, not_found_exception_handler, NotFoundException, \
    business_validation_exception_handler


def init_app():
    app = _init_fastapi_app()

    return app


def _init_fastapi_app():
    app = FastAPI(
        title='Imune',
        description='Imune API',
        version='0.0.1',
        redoc_url=None,
    )

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    routers = [user_router, login_router, vaccine_router, person_router]
    [app.include_router(**r) for r in routers]

    app.add_event_handler('startup', connect_to_mongo)
    app.add_event_handler("startup", apply_migrations)
    app.add_event_handler('shutdown', close_mongo_connection)

    app.add_exception_handler(NotFoundException, not_found_exception_handler)
    app.add_exception_handler(BusinessValidationException, business_validation_exception_handler)
    app.add_exception_handler(ApiBaseException, generic_render)
    app.add_exception_handler(EnvironmentException, generic_render)
    app.add_exception_handler(LoginException, generic_render)

    return app
