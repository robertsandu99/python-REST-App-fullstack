from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from fastapi import Depends, HTTPException, APIRouter, status
from models.models import User, Team
from schemas.schemas import UserCreate, UserGet, TeamCreate, TeamGet, TeamBase, UserBase
from repository.repository import TeamRepo, UserRepo
router = APIRouter()
from typing import List


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





############################### TEAMS ENDPOINTS #########################################


@router.post(
    "/teams", 
    response_model=TeamBase, 
    status_code=status.HTTP_201_CREATED
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


@router.get("/teams",
            response_model=List[TeamGet], 
            status_code=status.HTTP_200_OK
            )
async def get_list_teams(db_session: TeamRepo = Depends(TeamRepo)):
    teams_list = await db_session.get_all_teams()
    return teams_list


############################### USERENDPOINTS #########################################



@router.post(
    "/users", 
    response_model=UserGet, 
    status_code=status.HTTP_201_CREATED
)
async def create_new_user(
    new_user: UserCreate,
    db_session: UserRepo = Depends(UserRepo)
):
    try:
        created_user = await db_session.create_user(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    return created_user


@router.get("/users",
            response_model=List[UserGet], 
            status_code=status.HTTP_200_OK
            )
async def get_list_users(db_session: UserRepo = Depends(UserRepo)):
    users_list = await db_session.get_all_users()
    return users_list