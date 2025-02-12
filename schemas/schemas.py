from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserGet(UserBase):
    id: int
    team_id: Optional[int] = None


class User(UserBase):
    id: int
    team: Optional["TeamGet"] = None


class TeamBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class TeamGet(TeamBase):
    id: int


class TeamCreate(TeamBase):
    pass

class TeamUpdate(BaseModel):
    name: Optional[str]
