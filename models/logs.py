from beanie import Document
from pydantic import BaseModel, EmailStr

class Logs(Document):
    """
    Beanie document model. Handles validation for field types
    """
    time: int
    log: str

    class Settings:
        name = "logs" # Set collection name in database

class LogsData(BaseModel):
    """
    Pydantic model that acts as a projection model for return data
    """
    time: int
    log: str