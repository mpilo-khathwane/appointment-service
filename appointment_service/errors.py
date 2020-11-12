class ServiceException(Exception):

    def __init__(self, message=None, status_code=500):
        self.status_code = status_code
        self.message = message if message else "Service Error"

    def get_status_code(self):
        return self.status_code

    def to_dict(self):
        dto = {
            "status_code": self.status_code,
            "message": self.message
        }
        return dto


class ValidationException(ServiceException):
    def __init__(self, message=None):
        self.status_code = 400
        self.message = message if message else "Invalid value"


class RecordNotFoundException(ServiceException):
    def __init__(self, message=None):
        self.status_code = 404
        self.message = message if message else "Record not found"


class MethodNotAllowedException(ServiceException):
    def __init__(self, message=None):
        self.status_code = 405
        self.message = message if message else "Method Not Allowed"
