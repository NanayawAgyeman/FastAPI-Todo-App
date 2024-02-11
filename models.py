from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session
from database import Base
# from pydantic import BaseModel
from datetime import datetime


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    details = Column(String(100))
    created_at = Column(datetime)
    modified_at = Column(datetime)

# class ToDo(BaseModel):
#     id: int
#     title: str
#     details: str
#     created_at: datetime
#     modified_at: datetime

def create_todo(db: Session, title: str, details: str):
    todo = ToDo(title=title, details=details)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def get_todo(db: Session, todo_id: int):
    return db.query(ToDo).filter(ToDo.id == todo_id).first()

def update_todo(db: Session, todo_id: int, title: str, details: str):
    todo = get_todo(db, todo_id)
    if todo:
        todo.title = title
        todo.details = details
        db.commit()
        db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False
