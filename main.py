from datetime import date
from typing import Annotated
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

#read me

app = FastAPI(
    title="Student Management API",
    description="A RESTful API for managing university students.",
    version="1.0.0",
)

#data model

class Student(BaseModel):
    id: Optional[UUID] = None
    name:  str
    age: int
    email: str
    major: str
    gpa: float
    graduation: date

university: List[Student] = []

#enroll students

@app.post("/university/", response_model = Student, status_code=201)
async def register_student(stu: Student):
    stu.id = uuid4()
    university.append(stu)
    return stu

#find and filter students

@app.get("/university/", response_model = List[Student])
async def find_student(
    major: Optional[str] = Query(None, description = "filter students by major"),
    gpa: Optional[float] = Query(None, description= "filter students by GPA"),
    graduation: Optional[date] = Query(None, description= "filter students by graduation date"),
    sort_by: Optional[str] = Query(None, description = "sort by: name, major, gpa, graduation"),
    ):

    result = university.copy()

# filter
    if major:
        result = [student for student in result if major.lower() in student.major.lower()
        ]
    if gpa:
        result = [
             student for student in result
              if student.gpa == gpa
        ]
    if graduation:
        result = [
             student for student in result
               if student.graduation == graduation
        ]
# sorting

    if sort_by == "name":
        result = sorted(
            result,
            key=lambda student: student.name.lower()
        )
    if sort_by == "major":
            result = sorted(
                 result,
              key=lambda b: b.major.lower()
            )

    elif sort_by == "gpa":
            result = sorted(
                 result,
                   key= lambda s: s.gpa
                   )

    elif sort_by == "graduation":
            result = sorted(
                 result,
                   key= lambda s: s.graduation
                   )
    elif sort_by is not None:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort_by value. Use: name, major, gpa, graduation"
        )


    return result

#find student

@app.get("/university/{student_id}", response_model = Student)
async def get_student(student_id: UUID):
     for student in university:
          if student.id == student_id:
               return student
     raise HTTPException(status_code=404, detail= "student was not found")

#update student information

@app.put("/university/{student_id}", response_model = Student)
async def update_student(
     student_id: UUID,
     updated_student: Student
):
     for idx, student in enumerate(university):
             if student.id == student.id:
                  updated_student.id = student.id
                  university[idx] = updated_student
                  return updated_student


     raise HTTPException(status_code = 404, detail = "student was not found!")


# student Expulsion

@app.delete("/university/{student_id}", response_model= Student)
async def delete_student (student_id: UUID):
     for idx, student in enumerate(university):
          if student.id == student_id:
            expelled_student = university.pop(idx)
            return expelled_student

     raise HTTPException(status_code = 404, detail = "studnet was not found")

