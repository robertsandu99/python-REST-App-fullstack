from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int]
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass

    class Config:
        orm_mode = True


class User(UserBase):
    pass

    class Config:
        orm_mode = True


# class AssistantBase(BaseModel):
#     name: str

# class AssistantCreate(AssistantBase):
#     pass

# class Assistant(AssistantBase):
#     id: int
#     patients: List["Patient"] = []

#     class Config:
#         orm_mode = True

# class PatientBase(BaseModel):
#     name: str
#     age: int
#     assistant_id: int

# class PatientCreate(PatientBase):
#     pass

# class Patient(PatientBase):
#     id: int
#     assistant: Assistant

    class Config:
        orm_mode = True
