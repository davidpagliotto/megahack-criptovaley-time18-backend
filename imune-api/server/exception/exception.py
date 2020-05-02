from fastapi import Request
from fastapi.responses import JSONResponse


class ApiBaseException(Exception):
    status_code = 500
    message = None
    payload = None
    detail = None


class NotFound(Exception):
    def __init__(self, detail) -> None:
        self.detail = detail
        super().__init__()


class EnvironmentException(ApiBaseException):
    message = None
    payload = None
    detail = None

    def __init__(self, message=None, payload=None):
        self.message = message if message is not None else self.message
        ApiBaseException.__init__(self, self.message, payload)


async def not_found_exception_handler(request: Request, exc: NotFound):
    return JSONResponse(
        status_code=404,
        content={"detail": exc.detail},
    )
