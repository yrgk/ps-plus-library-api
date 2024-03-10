import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

from database import Base, engine
from models import Game


def parse_name_list():
    Base.metadata.create_all(engine)
    doc = requests.get("https://www.playstation.com/en-us/ps-plus/games/")
    soup = BeautifulSoup(doc.text, "html.parser")
    allnames = soup.find_all("a", {"module-name": "PS Plus Games List"})
    with Session(engine) as session:

        for name in allnames:

            doc = requests.get(name["href"])
            soup = BeautifulSoup(doc.text, "html.parser")
            parse_cover_url = soup.find_all("img")[1]
            parse_description = soup.find("p", {"data-qa": "mfe-game-overview#description"}).text
            parse_price = soup.find("span", {"data-qa": "mfeCtaMain#offer0#finalPrice"})
            publisher = soup.find("div", {"data-qa": "mfe-game-title#publisher"}).text
            release_date = soup.find("dd", {"data-qa": "gameInfo#releaseInformation#releaseDate-value"}).text

            if parse_price == None:
                parse_price = "Not available for purchase"
            else:
                parse_price = parse_price.text


            new_game = Game(
                name=name.text,
                price=parse_price,
                cover_url=parse_cover_url["src"],
                description=parse_description,
                publisher=publisher,
                release_date=release_date
            )

            session.add(new_game)
            session.commit()

            print(name.text)
    print("Success")

parse_name_list()