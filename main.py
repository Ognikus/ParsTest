import requests
from bs4 import BeautifulSoup

URL = 'https://stopgame.ru/topgames'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82\
 YaBrowser/21.9.0.1052 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
HOST = 'https://stopgame.ru'

def get_html (url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="item game-summary game-summary-horiz")

    game = []
    for item in items:
        game.append({
            'title': item.find('div', class_='caption caption-bold').get_text(strip=True),
            'link': HOST + item.find('div', class_='caption caption-bold').find_next('a').get('href'),
            'estimation': item.find('div', class_='value colored-bg-green').get_text(strip=True),
            'release_date': item.find('div', class_='game-specs').get_text(strip=True)
        })
    # print(items)
    print(game)

    # print(len(game))
    # return game

def parse():
     html = get_html(URL)
     if html.status_code == 200:
         get_content(html.text)
         # print(html.text)
     else:
         print("Error")

parse()