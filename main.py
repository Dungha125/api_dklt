from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import engine, SessionLocal, Base

# Tạo các bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency để lấy session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Các route
@app.post("/shifts/", response_model=schemas.ShiftResponse)
def register_shift(shift: schemas.ShiftCreate, db: Session = Depends(get_db)):
    return crud.create_shift(db, shift)

@app.get("/shifts/", response_model=list[schemas.ShiftResponse])
def read_shifts(db: Session = Depends(get_db)):
    return crud.get_shifts(db)

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
