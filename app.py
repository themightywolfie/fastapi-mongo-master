from fastapi import FastAPI

from config.config import initiate_database
from routes.logs import router as LogsRouter

app = FastAPI()

@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}

app.include_router(LogsRouter, tags=['Logs'])