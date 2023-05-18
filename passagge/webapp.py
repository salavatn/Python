from fastapi import FastAPI
import json

app = FastAPI(
    title="Internet Market",
    description="Work woth JSON",
    version="18.05.23",
)

@app.get("/api/json")
async def upload(json: dict):
    with open('data.json' , 'r') as file:
        data = json.load(file)

