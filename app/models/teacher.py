from sqlalchemy import Column, Integer, String
from ..database.db import Base

class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    
