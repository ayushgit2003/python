from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a Pydantic model for the request body
class UserRecommendedItem(BaseModel):
    userId: int
    skills: str
    jobTitles: str
    experienceLevel: str
    locations: str

# Create a POST route that expects a request body of type List[UserRecommendedItem]
@app.post("/user_recommendations/")
async def create_user_recommendations(user_recommended_list: List[UserRecommendedItem]):
    return user_recommended_list