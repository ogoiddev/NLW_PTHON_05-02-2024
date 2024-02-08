class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str = "Unprocessable Entity") -> None:
        super().__init__(message)
        self.name = "Unprocessable Entity"
        self.status_code = 422
        self.message = message
