class InvalidIdError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidTeamIdError(InvalidIdError):
    def __init__(self):
        message = "The team with the id requested does not exist"
        InvalidIdError.__init__(self, message)