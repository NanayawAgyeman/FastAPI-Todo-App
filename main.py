from fastapi import Depends
from fastapi import FastAPI, Form
from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from router import router
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Todo-App",
    description=f"Api documentation for NY Todo API",
    version="0.1.0",
)

templates = Jinja2Templates(directory="templates")

app.include_router(router)

@app.get("/")
async def index():
    return {"message": " Experience my todo api with me "}
