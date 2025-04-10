from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(55), nullable = False)
    email = Column(VARCHAR(255), unique=True, nullable = False)
    teams_id = Column(Integer, ForeignKey("teams.id"), nullable = True)

    team = relationship("Team", back_populates="user")

    __table_args__ = (
        UniqueConstraint('email', name='uniqu3_user_email'),
    )

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    user = relationship("User", back_populates="team", cascade="all, delete-orphan")


class UserHour(Base):
    __tablename__ = "users_hours"

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    hours = Column(Integer, nullable=False)
    user_name = Column(VARCHAR(255), nullable=False)
    overtime = Column(Integer, nullable=True)
    comment = Column(VARCHAR(255), nullable=True)

    user = relationship("User")
