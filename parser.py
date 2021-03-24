import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    request = requests.get(url)
    return request.text


def main():
    for i in range(1, 41):
        # проходимя по каждой странице и парсим содержимое по тегу <p>
        html = get_html(f'https://coinlib.io/api/v1/coinlist?\
            key=c76dcc904bccf9e7&pref=USD&page={str(i)}&order=rank')
        soup = bs(html, 'lxml')
        res = soup.find_all('p')

        for r in res:
            return r.text


if __name__ == '__main__':
    main()
