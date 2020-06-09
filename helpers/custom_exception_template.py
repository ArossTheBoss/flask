class CustomExceptionTemplate(Exception):
    """
    Custom exception class to allow more RESTFUL error to be returned.
    """
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code if status_code else 500
        self.payload = payload

    def to_dict(self):
        msg = dict(self.payload or ())
        msg['message'] = self.message
        return msg
