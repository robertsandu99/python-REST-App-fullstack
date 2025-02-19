from typing import List, Optional
from pydantic import BaseModel


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
