from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str
    email: str
    description: str

class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    id: int

    class Config:
        orm_mode = True
