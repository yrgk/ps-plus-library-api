from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Game
from schemas import GameBase
from library_parser import parse_name_list


app = FastAPI()

Base.metadata.create_all(engine)

# Routing
@app.get('/')
def main_page():
    return {"message": "Main page"}


@app.get('/games/all', response_model=list[GameBase])
def get_all_games(db: Session = Depends(get_db)):
    return db.query(Game).all()


@app.post('/games/update')
def update_all_games(db: Session = Depends(get_db)):
    game_list = parse_name_list()

    for game in game_list:
        new_game = Game(
            name = game[0],
            cover_url = game[1]
        )

        db.add(new_game)
        db.commit()

    return {"message": "Succes"}