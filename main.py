from fastapi import FastAPI, HTTPException
from typing import Dict, Any

app = FastAPI()

# Create a POST route that expects a request body of type Dict[Any, Any]
@app.post("/option3/")
async def option3(payload: Dict[Any, Any]): 
    return payload