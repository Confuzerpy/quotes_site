import requests
from bs4 import BeautifulSoup


url = 'https://api.cryptonator.com/api/full/btc-usd'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup