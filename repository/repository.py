from sqlalchemy import select, update
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.sql.expression import exists
from database.connection_db import async_session
from models.models import User, Team
from schemas.schemas import UserCreate, TeamCreate
from utils.exceptions import InvalidTeamIdError

# class UserRepo:
#     async def create_user(self, teams_id: int, user: UserCreate):
#         async with async_session() as session:
#             query = select(exists().where(Team.id == teams_id))
#             result_team = await session.execute(query)
#             if not result_team.scalar():
#                 raise InvalidTeamIdError
#             else:

#                 new_user = User(teams_id=teams_id, name=user.name, email=user.email)
#                 session.add(new_user)
#                 await session.commit()
#                 await session.refresh(new_user)
#                 return new_user
            

class TeamRepo:
    async def create_team(self, team: TeamCreate):
        async with async_session() as session:
            new_team = Team(name=team.name)
            session.add(new_team)
            await session.commit()
            await session.refresh(new_team)
            return new_team


