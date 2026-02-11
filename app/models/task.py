from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., example="Deploy new staging environment")
    description: Optional[str] = Field(
        None, 
        example="Provision VPS cluster and configure Nginx reverse proxy"
    )
    completed: bool = False
    created_at: Optional[datetime] = None
