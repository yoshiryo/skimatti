from pydantic import BaseModel

class Identity(BaseModel):
    spot_id: int
    session_id: str
    
