from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, ForeignKey, Integer, String
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(55), nullable = False)
    email = Column(VARCHAR(255), nullable = False)
    teams_id = Column(Integer, ForeignKey("teams.id"), nullable = True)

    teams = relationship("Team", back_populates="users", cascade="all, delete-orphan")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = True)

    users = relationship("User", back_populates="teams", cascade="all, delete-orphan")
