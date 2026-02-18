# models.py
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete")

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"))
    enrolled_at = Column(TIMESTAMP, server_default=func.now())

    __table_args__ = (UniqueConstraint("student_id", "course_id", name="unique_enrollment"),)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
