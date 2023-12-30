from bs4 import BeautifulSoup
import requests

def parse_name_list():
    namelist = []
    doc = requests.get("https://www.playstation.com/ru-ua/ps-plus/games/")
    soup = BeautifulSoup(doc.text, "html.parser")

    allnames = soup.find_all('p', class_='txt-style-base')

    for name in allnames:
        if name.find('a') is not None and name.text:
            namelist.append(name.text)
        # image = requests.get()
        # image = "hj"
        # print(f"{name.text()} : {image}")

    return namelist

for i in parse_name_list():
    print(i)