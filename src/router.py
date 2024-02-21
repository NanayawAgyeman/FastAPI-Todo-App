from fastapi import APIRouter, Depends, HTTPException
from src.database import get_db
from src.models import ToDo
from pydantic import BaseModel
from typing import List

router = APIRouter()


class ToDoIn(BaseModel):
    title: str
    details: str


@router.post("/todos/", response_model=ToDoIn)
def create_todo(todo_in: ToDoIn, info: dict = Depends(get_db)):
    return ToDo.create_todo(info=info, title=todo_in.title, details=todo_in.details)

@router.get("/todos/{todo_id}", response_model=ToDo)
def read_todo(todo_id: int, info: dict = Depends(get_db)):
    todo = ToDo.get_todo_item_by_id(info=info, todo_item_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/todos/", response_model=List[ToDo])
def read_all_todos(info: dict = Depends(get_db)):
    return ToDo.get_all_todo_items(info=info)

@router.put("/todos/{todo_id}", response_model=ToDo)
def update_todo(todo_id: int, todo_in: ToDoIn, info: dict = Depends(get_db)):
    todo = ToDo.update_todo(info=info, todo_id=todo_id, title=todo_in.title, details=todo_in.details)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, info: dict = Depends(get_db)):
    success = ToDo.delete_todo(info=info, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
