from bs4 import BeautifulSoup as bs
import requests
import json


def get_html(url):
    request = requests.get(url)
    return request.text


def coinlib_pars():
    result = []
    for i in range(1, 4):
        # проходим по каждой странице и парсим содержимое по тегу <p>
        html = get_html(
            f'https://coinlib.io/api/v1/coinlist?\
            key=c76dcc904bccf9e7&pref=USD&page={str(i)}&order=market_cap')
        soup = bs(html, 'lxml')
        res = soup.find_all('p')

        for r in res:
            result.append(json.loads(r.text))
            print('sparsil')
    return result


if __name__ == '__main__':
    coinlib_pars()
