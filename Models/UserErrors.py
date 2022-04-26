class UserNotFoundError(Exception):
    """
        Exception raised if a user is not found in database.
    """
    def __init__(self, msg):
        self.msg = msg
