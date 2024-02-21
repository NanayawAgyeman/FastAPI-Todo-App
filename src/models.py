from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from src.database import Base
from src.database import db
from datetime import datetime


class TodoModel(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    details = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, onupdate=datetime.now)


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "details": self.details,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }
    
    def create_todo(self) -> None:
        db.session.add(self)    
        db.session.commit()

    @classmethod
    def get_todo_item_by_id(cls,todo_item_id: int):
        return db.session.query(cls).filter_by(id=todo_item_id).first()
    
    @classmethod
    def get_all_todo_items_by_id(cls) -> list:
        return db.session.query(cls).all()
    
    def update_todo(self):
        db.session.commit()

    def delete_todo(self):
        db.session.delete(self)
        db.session.commit()
         
