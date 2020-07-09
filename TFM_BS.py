import requests
from bs4 import BeautifulSoup
req = requests.get('https://howlongtobeat.com/game?id=38019')
soup = BeautifulSoup(req.text, "lxml")
