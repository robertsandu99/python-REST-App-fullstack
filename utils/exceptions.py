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

class UserAlreadyAssignedError(InvalidIdError):
    def __init__(self):
        message = "The user is already assigned to this team"
        InvalidIdError.__init__(self, message)

class UserAlreadyReportedHours(InvalidIdError):
    def __init__(self):
        message = "User has already reported 8 hours for this day"
        InvalidIdError.__init__(self, message)

class CannotReportOnWeekendError(InvalidIdError):
    def __init__(self):
        message = "Cannot report hours on Saturday or Sunday"
        InvalidIdError.__init__(self, message)

class CannotReportMoreThanEight(Exception):
    def __init__(self, total_reported_hours, romania_date):
        self.message = f"Cannot add more than 8h/day. Currently you have {total_reported_hours}h on this date: {romania_date}"
