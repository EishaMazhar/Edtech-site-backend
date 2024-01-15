from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..crud import course as crud
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_409_CONFLICT,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_200_OK
)
from ..schemas.course import Course, CourseCreate
from ..database.db import SessionLocal, get_db

router = APIRouter()

@router.post("/courses/", response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)

@router.get("/courses/", response_model=List[Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@router.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Course not found")
    return  db_course                   

@router.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.update_course(db=db, course_id=course_id, course=course)

@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Course not found")
    crud.delete_course(db=db, course_id=course_id)
    return {"message":"deleted"}