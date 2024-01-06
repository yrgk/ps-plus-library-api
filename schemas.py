from pydantic import BaseModel, HttpUrl

class GameBase(BaseModel):
    id: int
    name: str
    cover_url: HttpUrl
    description: str

class GameBaseInList(BaseModel):
    id: int
    name: str
    cover_url: str
