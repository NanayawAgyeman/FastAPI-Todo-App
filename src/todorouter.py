from fastapi import APIRouter, Depends, HTTPException
from src.models import TodoModel
from pydantic import BaseModel
from typing import List
from typing import Annotated, Union
from datetime import datetime

todorouter = APIRouter()


class CreateTodoDTO(BaseModel):
    title: str
    details: str


@todorouter.post("/todos/")
async def create_todo(payload: CreateTodoDTO):
    todo_item = TodoModel(title=payload.title, details=payload.details)
    todo_item.create_todo()
    return todo_item.to_dict()


@todorouter.get("/todos/{todo_id}")
async def read_todo(todo_id: int):
    todo = TodoModel.get_todo_item_by_id(todo_item_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo.to_dict()


@todorouter.get("/todos/")
async def read_all_todos():
    todo_list = TodoModel.get_all_todo_items()
    if todo_list is None:
        raise HTTPException(status_code=404)
    return todo_list


class UpdateTodoDTO(BaseModel):
    id: int
    title: Union[str, None]
    details: Union[str, None]


@todorouter.put("/todo")
async def update_todo(payload: UpdateTodoDTO):
    todo_item = TodoModel.get_todo_item_by_id(payload.id)
    if todo_item is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_item.title = payload.title if payload.title else todo_item.title
    todo_item.details = payload.details if payload.details else todo_item.details
    todo_item.update_todo()
    return todo_item.to_dict()


@todorouter.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    todo_item = TodoModel.get_todo_item_by_id(todo_id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    try:
        todo_item.delete_todo()
    except HTTPException as e:
        raise HTTPException(status_code=404, detail="an Error occurred")
    return {"message": "Todo deleted successfully"}
