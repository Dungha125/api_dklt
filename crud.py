from sqlalchemy.orm import Session
from models import Shift, User
import schemas

def create_shift(db: Session, shift: schemas.ShiftCreate):
    new_shift = Shift(**shift.dict())
    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)
    return new_shift

def get_shifts(db: Session):
    return db.query(Shift).all()

def create_user(db: Session, user: schemas.UserCreate):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()
