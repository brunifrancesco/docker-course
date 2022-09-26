from fastapi import FastAPI
import os
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

app = FastAPI()

import motor.motor_asyncio
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_DETAILS = "mongodb://"+MONGO_HOST+":27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("students_collection")


from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
    }

# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

@app.post("/students", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")

@app.get("/students", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return ResponseModel([], "Empty list returned")

@app.get("/")
async def root():
    import socket
    return {"host": socket.gethostname()}
