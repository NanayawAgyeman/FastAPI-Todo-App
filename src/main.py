from fastapi import Depends
from fastapi import FastAPI, Form
from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from src.todorouter import router
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Todo-App",
    description=f"Api documentation for NY Todo API",
    version="0.1.0",
)

templates = Jinja2Templates(directory="templates")

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"], allow_headers=["Accept: application/json", "Content-Type: application/json"],
    allow_credentials=True,
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get("/")
async def index():
    return {"message": " Experience my todo api with me "}
