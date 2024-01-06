import time
from bs4 import BeautifulSoup
from fastapi import Depends, FastAPI
import requests
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Game
from schemas import GameBase, GameBaseInList
from library_parser import parse_name_list

from config import ADMIN_KEY as CURRENT_KEY

app = FastAPI()

Base.metadata.create_all(engine)

# Routing
@app.get('/')
def main_page():
    return {"message": "Main page"}


@app.get('/games/all', response_model=list[GameBaseInList])
def get_all_games(db: Session = Depends(get_db)):
    return db.query(Game).all()


@app.get('/games/{id}', response_model=GameBase)
def get_one_game(id: int, db: Session = Depends(get_db)):
    return db.query(Game).filter(Game.id == id).first()


@app.post('/games/update')
def update_all_games(admin_key: str, db: Session = Depends(get_db)):
    if admin_key == CURRENT_KEY:
        start = time.time()

        doc = requests.get("https://www.playstation.com/ru-ua/ps-plus/games/")
        soup = BeautifulSoup(doc.text, "html.parser")
        allnames = soup.find_all('a', {"module-name": "PS Plus Games List"})

        for name in allnames:
            doc = requests.get(name['href'])
            soup = BeautifulSoup(doc.text, "html.parser")

            try:
                photo_url = soup.find_all('img')[1]
            except:
                photo_url = soup.find_all('img')[0]
            description = soup.find('p', class_="psw-c-t-2 psw-p-x-7 psw-p-y-6 psw-p-x-6@below-tablet-s psw-m-sub-x-7 psw-m-auto@below-tablet-s psw-c-bg-card-1")

            if description == None:
                description.text = "There is no description"

            new_game = Game(
                name = name.text,
                cover_url = photo_url["src"],
                description = description.text
            )

            db.add(new_game)
            db.commit()

            print(new_game.name, "|", new_game.cover_url, "|", new_game.description)
            print("")

        end = time.time()
    else:
        return {"message": "Acces denied"}

    return {"message": "Succes", "Executing": (end - start)}