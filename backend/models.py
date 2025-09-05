from pydantic import BaseModel
from typing import Optional

class IdeaSubmission(BaseModel):
    title: str
    description: str
    file_url: Optional[str] = None
