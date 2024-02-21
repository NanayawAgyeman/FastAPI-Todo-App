from fastapi import APIRouter, Depends, HTTPException
from src.models import ToDo
from pydantic import BaseModel
from typing import List
from datetime import datetime

todorouter = APIRouter()


class ToDo(BaseModel):
    id: int
    title: str
    details: str
    created_at: datetime
    modified_at: datetime

@todorouter.post("/todos/", response_model=ToDo)
async def create_todo(todo_in: ToDo, info: dict = Depends()):
    return ToDo.create_todo(info=info, title=todo_in.title, details=todo_in.details)

@todorouter.get("/todos/{todo_id}", response_model=ToDo)
async def read_todo(todo_id: int, info: dict = Depends()):
    todo = ToDo.get_todo_item_by_id(info=info, todo_item_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@todorouter.get("/todos/")
async def read_all_todos(info: dict = Depends()):
    return ToDo.get_all_todo_items(info=info)

@todorouter.put("/todos/{todo_id}", response_model=ToDo)
async def update_todo(todo_id: int, todo_in: ToDo, info: dict = Depends()):
    todo = ToDo.update_todo(info=info, todo_id=todo_id, title=todo_in.title, details=todo_in.details)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@todorouter.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, info: dict = Depends()):
    success = ToDo.delete_todo(info=info, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
    