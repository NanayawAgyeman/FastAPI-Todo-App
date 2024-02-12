from pydantic import BaseModel
from datetime import datetime


class ToDo(BaseModel):
    id: int
    title: str
    details: str
    created_at: datetime
    modified_at: datetime