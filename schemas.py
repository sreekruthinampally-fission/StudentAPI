# schemas.py
from pydantic import BaseModel
from typing import List

# Request
class StudentCreate(BaseModel):
    name: str
    email: str

class CourseCreate(BaseModel):
    title: str
    description: str

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

# Response
class StudentOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # Pydantic v2

class CourseOut(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    courses: List[CourseOut]

    class Config:
        from_attributes = True
