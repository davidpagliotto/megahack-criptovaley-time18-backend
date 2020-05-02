from fastapi import Request
from fastapi.responses import JSONResponse


class ApiBaseException(Exception):
    status_code = 500
    message = None
    payload = None
    detail = None


class EnvironmentException(ApiBaseException):
    message = None
    payload = None
    detail = None

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)


class BusinessValidationException(Exception):
    def __init__(self, detail) -> None:
        self.detail = detail
        super().__init__()


class NotFoundException(Exception):
    def __init__(self, detail) -> None:
        self.detail = detail
        super().__init__()


async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": exc.detail},
    )


async def business_validation_exception_handler(request: Request, exc: BusinessValidationException):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.detail},
    )
