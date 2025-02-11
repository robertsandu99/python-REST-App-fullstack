from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import User, Team
#from schemas.schemas import PatientCreate, AssistantCreate

router = APIRouter()

DATABASE_URL = 'postgresql://postgres:asdasd@localhost:5432/HourTracking'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@router.get("/")
async def root():
    return {"message": "Hello World"}

async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
@router.post("/assistants/")
async def create_assistant(
    assistant: AssistantCreate, db: Session = Depends(get_db)
):
    db_assistant = Assistant(name=assistant.name)
    db.add(db_assistant)
    db.commit()
    db.refresh(db_assistant)
    return db_assistant
