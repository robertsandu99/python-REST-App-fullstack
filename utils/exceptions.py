from fastapi import HTTPException

# class InvalidUserIdError(HTTPException):
#     def __init__(self):
#         super().__init__(status_code=404, detail="The user with the id requested does not exist")

# class UserAlreadyAssignedError(HTTPException):
#     def __init__(self):
#         super().__init__(status_code=400, detail="The user is already assigned to this team")

# class InvalidTeamIdError(HTTPException):
#     def __init__(self):
#         super().__init__(status_code=404, detail="The team with the id requested does not exist")


class InvalidIdError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidUserIdError(InvalidIdError):
    def __init__(self):
        message = "The user with the id requested does not exist"
        InvalidIdError.__init__(self, message)

class InvalidTeamIdError(InvalidIdError):
    def __init__(self):
        message = "The team with the id requested does not exist"
        InvalidIdError.__init__(self, message)

class UserAlreadyAssignedError(HTTPException):
    def __init__(self):
        message = "The user is already assigned to this team"
        InvalidIdError.__init__(self, message)
