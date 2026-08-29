from datetime import date
from typing import Annotated
from fastapi import FastAPI, HTTPEXception, Query
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI()

class Student(BaseModel):
    id: Optional[UUID] = None
    name:  str
    age: int
    email: str
    major: str
    gpa: float
    graduation: date

university: List[Student] = []


@app.post("/university/", response_model = Student)
async def register_student(stu: Student):
    stu.id = uuid4()
    university.append(stu)
    return stu

@app.get("/university/", response_model = List[Student])
async def find_student(N: Annotated[str|None, Query(maximum_length = 50)] = None):
    sort_by: Optional[str] = Query(None),
    major: Optional[str] = Query(None, description = "sort by major"),
    gpa: Optional[int] = Query(None, description= "sort by gpa"),
    graduation: Optional[date] = Query(None, description= "sort by graduation")
    result = university.copy()

# filter
    if major:
        result = [
             student for student in result
               major.lower() in student.major.lower()

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

    if sort_by == "major":
            result = sorted(result, key=lambda b: b.major.lower())
    elif sort_by == "gpa":
            result = sorted(result, key= lambda s: s.gpa)

    elif sort_by == "graduation":
            result = sorted(result, key= lambda s: s.graduation)

    return university


@app.get("/university/{student_id}", response_model=Student)
def search_student(student_id: UUID):

    for student in university:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code= 404,
        detail="Student was not found!"
    )

@app.put("/university/{student_name}", response_model = Student)
def update_student(student_name : Optional[str] = None, modify_student: Student):
     for idx, Studnet in enumerate(university):
        if Student.name == student.name:
             update_student = Student.copy(update = modify_student.update.dict(exclude_unset = True))
             university[idx] = update_student
        return update_studentg
        raise HTTPException(
             status_code = 404,
             detail = "student was not found!"
        )

@app.put("/university/{student_gpa}", response_model= Student)
def

     major: Optional[] = None
     gpa: Optional[] = None
     graduation: Optional[] = None

@app.delete("/university/{student_id}", response_model= Student)
def delete_student (student_id: UUID, del_student: Student)
     for idx, Student in enumerate(university):
          if Student.id == student_id:
            reject_student = Student.copy(update = student_id.update.dict(exclude_unset = True))
            university[idx] = reject_student
          return reject_student
          raise HTTPEXception(
               status_code = 404,
               detail = " studnet was not found"
          )

