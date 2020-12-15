from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Topics(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, unique=True, index=True)

    questions = relationship("Questions", back_populates="owner")


class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id"))

    owner = relationship("Topics", back_populates="questions")


class Topic(str, Enum):
    random = 'random'
    tv = 'tv'
    apps = 'apps'
    books = 'books'
    clothes = 'clothes'
    education = 'education'
    deep = 'deep'
    food = 'food'
    funny = 'funny'
    goals = 'goals'
    holidays = 'holidays'
    light = 'light'
    movies = 'movies'
    music = 'music'
    phones = 'phones'
    restaurants = 'restaurants'
    romantic = 'romantic'
    seasons = 'seasons'
    sports = 'sports'
    technology = 'technology'
    travel = 'travel'
    weird = 'weird'
