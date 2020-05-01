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
