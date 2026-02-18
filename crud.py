# crud.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def create_course(db: Session, course: schemas.CourseCreate):
    new_course = models.Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

def enroll_student(db: Session, enroll: schemas.EnrollmentCreate):
    student = db.query(models.Student).filter_by(id=enroll.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    course = db.query(models.Course).filter_by(id=enroll.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    existing = db.query(models.Enrollment).filter_by(
        student_id=enroll.student_id,
        course_id=enroll.course_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already enrolled")
    enrollment = models.Enrollment(**enroll.dict())
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)
    return enrollment

def get_student_with_courses(db: Session, student_id: int):
    student = db.query(models.Student).filter_by(id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    courses = [en.course for en in student.enrollments]
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "courses": courses
    }
