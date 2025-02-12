from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, HTTPException, APIRouter, status
from models.models import User, Team
from schemas.schemas import UserCreate, UserGet, TeamCreate, TeamGet, TeamBase, UserBase
from repository.repository import TeamRepo
router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


# @router.post("/users/",
#             response_model=UserCreate,
#             status_code=status.HTTP_201_CREATED)

# async def create_user(
#     user: UserCreate,
#     db: Session = Depends(get_db)
#     ):

#     db_user = User(name=user.name, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user        

# @router.post("/users/")
# async def create_assistant(
#     assistant: AssistantCreate, db: Session = Depends(get_db)
# ):
#     db_assistant = Assistant(name=assistant.name)
#     db.add(db_assistant)
#     db.commit()
#     db.refresh(db_assistant)
#     return db_assistant
@router.post(
    "/teams", response_model=TeamBase, status_code=status.HTTP_201_CREATED
)
async def create_new_team(
    newteam: TeamCreate,
    db_session: TeamRepo = Depends(TeamRepo)
):
    try:
        created_team = await db_session.create_team(newteam)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="This team name already exists")
    return created_team
