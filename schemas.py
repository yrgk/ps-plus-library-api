from pydantic import BaseModel, HttpUrl

class GameBase(BaseModel):
    id: int
    name: str
    cover_url: HttpUrl