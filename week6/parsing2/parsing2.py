from typing import List, Dict, Callable

import bs4.element
import requests
import json
from bs4 import BeautifulSoup


def clear_text(text: str):
    return text.replace('\n', '').strip()


def handle_attr_err(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return clear_text(func(*args, **kwargs))
        except AttributeError:
            return ''
    return wrapper


def open_json() -> List:
    with open('data.json') as json_file:
        return json.load(json_file)


def write_to_json(data: Dict):
    db = open_json()
    db.append(data)
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(db, indent=2))


def get_html(url: str) -> bytes:
    print('GET:', url)
    res = requests.get(url)
    return res.content


def get_data(html: bytes) -> bool:
    soup = BeautifulSoup(html, 'lxml')

    try:
        cars_list_html = soup.find('div', class_='catalog-list').find_all(class_='catalog-list-item')
    except AttributeError:
        return False

    @handle_attr_err
    def get_year(car_tag: bs4.element.Tag) -> str:
        return car_tag.find(class_='caption-year').text

    @handle_attr_err
    def get_title(car_tag: bs4.element.Tag, year_to_replace: str) -> str:
        return car_tag.find(class_='catalog-item-caption').text.replace(year_to_replace, '')

    @handle_attr_err
    def get_img(car_tag: bs4.element.Tag) -> str:
        return car_tag.find('img').attrs.get('src')

    @handle_attr_err
    def get_millage(car_tag: bs4.element.Tag) -> str:
        return clear_text(car_tag.find(class_='catalog-item-mileage').text)

    @handle_attr_err
    def get_dollar_price(car_tag: bs4.element.Tag) -> str:
        return clear_text(car_tag.find(class_='catalog-item-price').text)

    @handle_attr_err
    def get_som_price(car_tag: bs4.element.Tag) -> str:
        return clear_text(car_tag.find(class_='catalog-item-price').attrs.get('title'))

    @handle_attr_err
    def get_descr(car_tag: bs4.element.Tag) -> str:
        return ' '.join(clear_text(car_tag.find(class_='catalog-item-descr').text).split())

    @handle_attr_err
    def get_date(car_tag: bs4.element.Tag) -> str:
        return clear_text(car_tag.find(class_='catalog-item-info').text)

    @handle_attr_err
    def get_link(car_tag: bs4.element.Tag) -> str:
        return 'https://cars.kg' + car_tag.attrs.get('href')

    for car in cars_list_html:
        year = get_year(car)
        write_to_json({
            'title': get_title(car, year),
            'millage': get_millage(car),
            'dollar_price': get_dollar_price(car),
            'som_price': get_som_price(car),
            'descr': get_descr(car),
            'date': get_date(car),
            'img': get_img(car),
            'link': get_link(car),
        })

    return True


def main():
    i = 1
    while True:
        url = 'https://cars.kg/offers/'
        res = get_html(url+str(i))

        print(f'Parsing started page: {i}')
        data = get_data(res)

        if not data:
            break

        i += 1


with open('data.json', 'w') as file:
    file.write(json.dumps([], indent=2))


main()
