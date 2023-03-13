class MissingArguments():
    def __init__(self):
        self.status = 400,
        self.type = "Missing Arguments",
        self.details = "There are missing items in the request body"

class RequestValidationError():
    def __init__(self):
        self.status = 406,
        self.type = "Not Acceptable",
        self.details = "The request body was not a valid JSON string"


class InternalServerError():
    def __init__(self):
        self.status = 500,
        self.type = "Internal Server Error",
        self.details = "The server is unable to handle your request at this time"
