from fastapi import FastAPI, HTTPException
from typing import Dict, Any
from union import union
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List
import asyncio

# app = FastAPI()

# # Create a POST route that expects a request body of type Dict[Any, Any]
# @app.post("/option3/")
# async def option3(payload: Dict[Any, Any]): 
#     return payload


# app = FastAPI()

# # MongoDB connection details
# MONGO_DETAILS = "mongodb+srv://ayush:user@cluster0.f2dpvrq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = AsyncIOMotorClient(MONGO_DETAILS)
# database = client["test"]
# collection = database["jobpreferences"]
# collectionJob=database["jobposts"]

# # Pydantic model for response
# class Item(BaseModel):
#     userId: int
#     skills: List[str]  # Updated to a list of strings
#     jobTitles: List[str]  # Updated to a list of strings
#     experienceLevel: str
#     locations: List[str]  # Updated to a list of strings

# class JobItem(BaseModel):
#     jobId: int
#     companyName: str
#     jobTitle: str
#     jobType: str
#     jobSkills: List[str]
#     jobDescription: str
#     jobExperienceLevel: str
#     jobLocation: str
#     jobSalary: str

# @app.get("/items/", response_model=List[Item])
# async def get_items():
#     items = await collection.find().to_list(1000)  # Adjust the limit as needed
#     jobs=await collectionJob.find().to_list(1000)
#     union(items,jobs)
#     if not items:
#         raise HTTPException(status_code=404, detail="Items not found")
#     return items


app = FastAPI()

# MongoDB connection details
MONGO_DETAILS = "mongodb+srv://ayush:user@cluster0.f2dpvrq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["test"]
collection = database["jobpreferences"]
collectionJob = database["jobposts"]

# Pydantic model for response
class Item(BaseModel):
    userId: int
    skills: List[str]  # Updated to a list of strings
    jobTitles: List[str]  # Updated to a list of strings
    experienceLevel: str
    locations: List[str]  # Updated to a list of strings

class JobItem(BaseModel):
    jobId: int
    companyName: str
    jobTitle: str
    jobType: str
    jobSkills: List[str]
    jobDescription: str
    jobExperienceLevel: str
    jobLocation: str
    jobSalary: str

async def fetch_data():
    items = await collection.find().to_list(1000)  # Adjust the limit as needed
    jobs = await collectionJob.find().to_list(1000)
    union(items, jobs)

async def call_api_every_two_minutes():
    while True:
        await fetch_data()
        await asyncio.sleep(30)  # Sleep for 120 seconds (2 minutes)

@app.get("/items/", response_model=List[Item])
async def get_items():
    items = await collection.find().to_list(1000)  # Adjust the limit as needed
    if not items:
        raise HTTPException(status_code=404, detail="Items not found")
    return items

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(call_api_every_two_minutes())


