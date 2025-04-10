from sqlalchemy.exc import IntegrityError
from fastapi import Depends, HTTPException, APIRouter, status
from schemas.schemas import UserCreate, UserGet, TeamCreate, TeamGet, TeamBase, UserBase, UserPut, UserHourGet, UserHourCreate
from repository.repository import TeamRepo, UserRepo, UserHourRepo
from typing import List
from utils.exceptions import InvalidUserIdError, InvalidTeamIdError, UserAlreadyAssignedError, UserAlreadyReportedHours, CannotReportOnWeekendError, CannotReportMoreThanEight



router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


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


############################### USER ENDPOINTS #########################################



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
async def get_list_users(
    db_session: UserRepo = Depends(UserRepo)
    ):
    users_list = await db_session.get_all_users()
    return users_list


@router.put(
    "/users/{user_id}/assign-to-team/{team_id}", 
    response_model=UserPut, 
    status_code=status.HTTP_200_OK
    )
async def assign_user_to_team(
    user_id: int,
    teams_id: int,
    db_session: UserRepo = Depends(UserRepo)
    ):
    try:
        assigned_user = await db_session.assign_user_to_team(user_id, teams_id)
    except InvalidUserIdError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except InvalidTeamIdError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except UserAlreadyAssignedError as e:
        raise HTTPException(status_code=400, detail=e.message)
    return assigned_user

############################## USERS_HOURS ##############################################

@router.post(
    "/hours/{users_id}", 
    response_model=UserHourGet,
    status_code=status.HTTP_201_CREATED
    )
async def add_hours_for_users(
    users_id: int,
    userhour: UserHourCreate,
    db_session: UserHourRepo = Depends(UserHourRepo)
    ):
    try:
        added_user_hours = await db_session.create_user_hour(users_id, userhour)
    except InvalidUserIdError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except IntegrityError:
        raise HTTPException(status_code=400)
    except UserAlreadyReportedHours as e:
        raise HTTPException(status_code=400, detail=e.message)
    except CannotReportOnWeekendError as e:
        raise HTTPException(status_code=400, detail=e.message)
    except CannotReportMoreThanEight as e:
        raise HTTPException(status_code=400, detail=e.message)
    return added_user_hours
