from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Session
from src.database import Base
from datetime import datetime


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    details = Column(String(100))
    created_at = Column(Date, default=datetime.now)
    modified_at = Column(Date, onupdate=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }

    @staticmethod
    def create_todo(db: Session, title: str, details: str):
        todo = ToDo(title=title, details=details)
        db.add(todo)
        db.commit()
        return todo

    @classmethod
    def get_todo_item_by_id(cls, db: Session, todo_item_id: int):
        return db.query(cls).filter_by(id=todo_item_id).first()
    
    @classmethod
    def get_all_todo_items_by_id(cls, db: Session, id: int) -> list:
        return db.query(cls).all()
    
    @staticmethod
    def update_todo(db: Session, todo_id: int, title: str, details: str):
        todo = ToDo.get_todo_item_by_id(db, todo_id)
        if todo:
            todo.title = title
            todo.details = details
            db.commit()
        return todo

    @staticmethod
    def delete_todo(db: Session, todo_id: int):
        todo = ToDo.get_todo_item_by_id(db, todo_id)
        if todo:
            db.delete(todo)
            db.commit()
            return True
        return False
