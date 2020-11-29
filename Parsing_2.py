import requests
from bs4 import BeautifulSoup
import urllib

print('Search the: ')
search = urllib.parse.quote(input())
URL = 'https://play.google.com/store/search?q=' + search + '&c=apps&hl=ru'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36', 'accept': '*/*'}
HOST = 'https://play.google.com'

def _get_html(url, params=None):
    html = requests.get(url, headers=HEADERS, params=params)
    return html

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    games = soup.find_all('div', class_='ImZGtf mpg5gc')

    data = []
    for game in games:
        data.append({
            'title': game.find('div', class_='WsMG1c nnK0zc').get_text(strip=True),
            'link' : HOST + game.find('a', class_='JC71ub').get('href'),
            'img'  : game.find('img', class_='T75of QNCnCf').get('data-srcset')[:len(game.find('img', class_='T75of QNCnCf').get('data-srcset'))-3],
            'price': content_price(game.find('span', class_='VfPpfd ZdBevf i5DZme'))
        })
    return data

def content_price(str):
    if(str==None):
        return 'Free'
    else:
        return str.get_text()[:len(str.get_text())-2]+'₽'


def parse():
    html = _get_html(URL)
    if html.status_code == 200:
        data = get_content(html.text)
        print(data)
    else:
        print('Error')


parse()