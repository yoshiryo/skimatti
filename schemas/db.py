from sqlite3 import dbapi2
from pydantic import BaseModel

class DB(BaseModel):
    user: str
    passwd: str
    host: str
    db: str
    charset: str
