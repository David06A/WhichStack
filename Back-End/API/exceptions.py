class MissingArguments():
    def __init__(self):
        self.status_code = 400,
        self.body = {
            "error_message": "Missing Arguments",
            "error_details": "There are missing items in the request body"
        }

class RequestValidationError():
    def __init__(self):
        self.status_code = 406,
        self.body = {
            "error_message": "Not Acceptable",
            "error_details": "The request body was not a valid JSON string"
        }

class InternalServerError():
    def __init__(self):
        self.status_code = 500,
        self.body = {
            "error_message": "Internal Server Error",
            "error_details": "The server is unable to handle your request at this time"
        }
