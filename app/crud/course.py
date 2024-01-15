from sqlalchemy.orm import Session
from ..models.course import Course
from ..schemas.course import CourseCreate


def get_course(db: Session, course_id:int):
    return db.query(Course).filter(Course.id==course_id).first()

def get_courses(db:Session, skip:int=0, limit:int=1000):
    # return db.query(Course).offset(skip).limit(limit).all() #use this when you want to specify a range
    return db.query(Course).all()

def create_course(db: Session, course: CourseCreate):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: CourseCreate):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        db_course.title = course.title
        db_course.description = course.description
        db.commit()
        db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course