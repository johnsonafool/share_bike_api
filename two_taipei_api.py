from fastapi import FastAPI, HTTPException
from typing import List
import os
import json

app = FastAPI()

# data is based on 
# Path to your 'taipei' folder
data_folder = "./two_taipei"

@app.get("/files/", response_model=List[str])
async def list_files():
    """List all JSON files in the directory."""
    files = [f for f in os.listdir(data_folder) if f.endswith('.json')]
    return files

@app.get("/files/{filename}", response_model=dict)
async def read_file(filename: str):
    """Read and return the content of a specific JSON file."""
    file_path = os.path.join(data_folder, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

