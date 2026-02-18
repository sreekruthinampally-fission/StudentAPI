# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, schemas, models
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Course Enrollment API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.post("/courses", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@app.post("/enrollments")
def enroll_student(enroll: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    return crud.enroll_student(db, enroll)

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student_with_courses(db, student_id)
