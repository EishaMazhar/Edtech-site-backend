from fastapi import FastAPI
from pydantic import BaseModel
from .api.course import router as course_router
from .api.teacher import router as teacher_router

from .database.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Edtech site Backend")

@app.get("/")
def read_root():
    return {"title": "An online Learning Platform"}

app.include_router(course_router)
app.include_router(teacher_router)
