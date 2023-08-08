import datetime

from database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    task = Column(String(255))
    done = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now())

