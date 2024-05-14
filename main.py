from fastapi import FastAPI, HTTPException
from typing import Dict, Any

app = FastAPI()

# Create a POST route that expects a request body of type Dict[Any, Any]
@app.post("/option3/")
async def option3(payload: Dict[Any, Any]): 
    # Extract the "input" part from the payload
    input_data = payload.get("input")
    if input_data is None:
        raise HTTPException(status_code=400, detail="No 'input' found in the payload")
    
    return input_data