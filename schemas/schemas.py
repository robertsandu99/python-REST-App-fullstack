from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass


class UserGet(UserBase):
    id: int
    teams_id: Optional[int] = None


class UserPut(UserBase):
    id: int
    teams_id: int


class User(UserBase):
    id: int
    teams_id: Optional["TeamGet"] = None


class TeamBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class TeamGet(TeamBase):
    id: int


class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    name: Optional[str]


class UserHourGet(BaseModel):
    id: int
    users_id: int
    user_name: str
    date: date
    hours: int
    overtime: int
    comment: str

    class Config:
        from_attributes = True

class UserHourCreate(BaseModel):
    date: date
    hours: int
    overtime: Optional[int] = None
    comment: Optional[str] = None

    class Config:
        from_attributes = True