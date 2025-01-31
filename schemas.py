from pydantic import BaseModel
from typing import Optional

class ShiftBase(BaseModel):
    day_of_week: str
    time_slot: str
    user_id: Optional[int] = None

class ShiftCreate(ShiftBase):
    pass

class ShiftResponse(ShiftBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
