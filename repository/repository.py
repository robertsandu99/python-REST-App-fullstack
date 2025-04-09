from sqlalchemy import select, update
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.sql.expression import exists
from database.connection_db import async_session
from models.models import User, Team, UserHour
from schemas.schemas import UserCreate, TeamCreate, UserHourCreate
from utils.exceptions import InvalidUserIdError, UserAlreadyAssignedError, InvalidTeamIdError
from datetime import datetime, timedelta
from fastapi import HTTPException


class TeamRepo:
    async def create_team(self, team: TeamCreate):
        async with async_session() as session:
            new_team = Team(name=team.name)
            session.add(new_team)
            await session.commit()
            await session.refresh(new_team)
            return new_team
        
    async def get_all_teams(self):
        async with async_session() as session:
            select_teams = await session.execute(select(Team))
            all_teams = select_teams.scalars().all()
            return all_teams

class UserRepo:
    async def create_user(self, user: UserCreate):
        async with async_session() as session:
            new_user = User(name=user.name, email=user.email)
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def get_all_users(self):
        async with async_session() as session:
            select_users = await session.execute(select(User))
            all_users = select_users.scalars().all()
            return all_users

    async def assign_user_to_team(self, user_id: int, teams_id: int):
        async with async_session() as session:
            user = await session.get(User, user_id)
            if not user:
                raise InvalidUserIdError
            
            team = await session.get(Team, teams_id)
            if not team:
                raise InvalidTeamIdError
            
            if user.teams_id == teams_id:
                raise UserAlreadyAssignedError
            else:
                user.teams_id = teams_id
                await session.commit()
                await session.refresh(user)
                return user
    

# class UserHourRepo:
#     async def create_user_hour(self, users_id: int, userhour: UserHourCreate):
#         async with async_session() as session:
#             query_user = select(exists().where(User.id == users_id))
#             result_user = await session.execute(query_user)

#             if not result_user.scalar():
#                 raise InvalidUserIdError
#             else:
#                 new_userhour = UserHour(users_id=users_id, date=userhour.date.replace(tzinfo=None), hours=userhour.hours, comment=userhour.comment)
#                 print(new_userhour)
#                 session.add(new_userhour)
#                 await session.commit()
#                 return new_userhour
            


class UserHourRepo:
    async def create_user_hour(self, users_id: int, userhour: UserHourCreate):
        async with async_session() as session:
            query_user = select(User).where(User.id == users_id)
            result_user = await session.execute(query_user)
            user_obj = result_user.scalar()
            
            if not user_obj:
                raise InvalidUserIdError
            
            # Romania timezone
            updated_date = userhour.date + timedelta(hours=3)

            new_userhour = UserHour(
                users_id=users_id,
                date=updated_date.replace(tzinfo=None),
                hours=userhour.hours,
                overtime=userhour.overtime,
                comment=userhour.comment,
                user_name=user_obj.name 
            )
            session.add(new_userhour)
            await session.commit()
            return new_userhour


    #  async def update_user(self, user_id: int, user_data: UserCreate):
    #     async with async_session() as session:
    #         user = await session.get(User, user_id)
    #         if not user:
    #             raise HTTPException(status_code=404, detail="User not found")
            
    #         # Update user fields
    #         user.name = user_data.name
    #         user.email = user_data.email

    #         # If a team is provided in user_data, update the team association
    #         if user_data.team_id:
    #             user.teams_id = user_data.team_id
    #         else:
    #             user.teams_id = None  # If no team, remove the assignment

    #         session.add(user)
    #         await session.commit()
    #         await session.refresh(user)
    #         return user
