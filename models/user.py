from _datetime import datetime
from typing import Any

from sqlalchemy import String, BigInteger, Column, DateTime, ForeignKey
from models.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    full_name = Column(String)
    phone = Column(String)
    role = Column(String)
    status = Column(String, default="открыто")
    registered_at = Column(DateTime, default=datetime)
    last_activity = Column(DateTime)

class Categories(Base):
    __tablename__ = "categories"
    id = Column(BigInteger, primary_key=True)
    title = Column(String(250))
    description = Column(String(320))

class Requests(Base):
    __tablename__ = "requests"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
