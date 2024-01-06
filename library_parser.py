import time
import requests
from bs4 import BeautifulSoup


def parse_name_list():

    start = time.time()

    doc = requests.get("https://www.playstation.com/ru-ua/ps-plus/games/")
    soup = BeautifulSoup(doc.text, "html.parser")
    allnames = soup.find_all('a', {"module-name": "PS Plus Games List"})

    game_list = []

    for name in allnames:
        doc = requests.get(name['href'])
        soup = BeautifulSoup(doc.text, "html.parser")
        photo_url = soup.find_all('img')[1]
        description = soup.find('p', class_="psw-c-t-2 psw-p-x-7 psw-p-y-6 psw-p-x-6@below-tablet-s psw-m-sub-x-7 psw-m-auto@below-tablet-s psw-c-bg-card-1")

        game_list.append((name.text, photo_url['src'], description.text))
        print([name.text, photo_url['src']], description.text)
        print("")
    return game_list
# parse_name_list()