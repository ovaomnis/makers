from typing import List, Dict

import bs4
import requests
from bs4 import BeautifulSoup
import json


def open_db() -> List:
    try:
        with open('data.json') as file:
            return json.load(file)
    except FileNotFoundError:
        with open('data.json', 'w+') as file:
            file.write('[]')
            file.seek(0)
            return json.load(file)


def add_records(data: List[dict]) -> None:
    db = open_db()
    db.extend(data)
    with open('data.json', 'w') as file:
        file.write(json.dumps(db, indent=2))


def get_html(url: str):
    headers = {'Accept-Charset': 'utf-8'}
    response = requests.get(url, headers=headers)
    return response.text


def get_data(html: str):
    soup = BeautifulSoup(html, 'lxml')
    laptops = []
    for i in soup.find_all(class_='product_listbox'):
        title = i.find(class_='listbox_title').text.strip()
        laptops.append(
            {
                'title': title,
                'price': i.find(class_='listbox_price').find('strong').text,
                'text': i.find(class_='product_text').text.replace(title, '').strip(),
                'link': 'https://www.kivano.kg' + i.find('a').attrs.get('href', None),
                'img': 'https://www.kivano.kg' + i.find('img').attrs.get('src', None)
            }
        )
    return laptops


def get_pages(html: str):
    soup = BeautifulSoup(html, 'lxml')
    return int(soup.find('ul', class_='pagination').find('li', class_='last').text)


def clear_text(text: str) -> str:
    return text.replace('\n', '').strip()


def main():
    url = 'https://www.kivano.kg/noutbuki'
    pages = get_pages(get_html(url))
    print("Page detected:", pages)
    for i in range(1, pages + 1):
        print('parsing page', i)
        url_with_page = f'{url}?page{i}'
        add_records(get_data(get_html(url_with_page)))


if __name__ == '__main__':
    main()
