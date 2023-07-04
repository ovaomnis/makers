from typing import List

import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com'
    }
    return requests.get(url, headers=headers).text


def get_data(html: str) -> List[dict]:
    movie_set = []
    soup = BeautifulSoup(html, 'lxml')

    for movie in soup.find('ul', attrs={'class': 'ipc-metadata-list ipc-metadata-list--dividers-between sc-3a353071-0 wTPeg compact-list-view ipc-metadata-list--base'}).find_all('a'):
        movie_set.append({
                'name': movie.text,
                'link': 'https://www.imdb.com' + movie.attrs.get('href')
            })
    return movie_set


def get_link(title_list: List[dict], keyword: str):
    for title in title_list:
        if title.get('name').lower().count(keyword.lower()):
            return title.get('link')


def main():
    url = 'https://www.imdb.com/chart/top/'
    title_list = get_data(get_html(url))
    print(get_link(title_list, 'shawshank'))


if __name__ == '__main__':
    main()
