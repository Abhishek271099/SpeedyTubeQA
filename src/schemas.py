from pydantic import BaseModel
from typing import Optional

class InputSchema(BaseModel):
    question: str
    youtube_link: Optional[str] = None


class OutputSchema(BaseModel):
    response: str
    class Config:
        from_attributes = True