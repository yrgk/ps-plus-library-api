from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Game
from schemas import GameBase, GameBaseInList

app = FastAPI()

Base.metadata.create_all(engine)

# Routing

@app.get('/')
def main():
    return "main page"

@app.get("/games/all", response_model=list[GameBaseInList])
def get_all_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Game).offset(skip).limit(limit).all()


@app.get("/games/{id}", response_model=GameBase)
def get_one_game(id: int, db: Session = Depends(get_db)):
    return db.query(Game).filter(Game.id == id).first()