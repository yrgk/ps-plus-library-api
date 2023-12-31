import requests
from bs4 import BeautifulSoup


def parse_name_list():
    doc = requests.get("https://www.playstation.com/ru-ua/ps-plus/games/")
    soup = BeautifulSoup(doc.text, "html.parser")
    allnames = soup.find_all('a', {"module-name": "PS Plus Games List"})

    game_list = []

    for name in allnames:
        doc = requests.get(name['href'])
        soup = BeautifulSoup(doc.text, "html.parser")
        photo_url = soup.find_all('img')[1]

        game_list.append((name.text, photo_url['src']))
        print([name.text, photo_url['src']])
    return game_list