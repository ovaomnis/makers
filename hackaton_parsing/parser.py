import json
from typing import List, Callable

import bs4.element
import requests
from bs4 import BeautifulSoup as Bs


def clear_text(text: str):
    return text.replace('\n', '').strip()


def try_get(func) -> Callable[[bs4.element.Tag], str]:
    def wrapper(article: bs4.element.Tag, *args, **kwargs) -> str:
        try:
            return func(article, *args, **kwargs)
        except AttributeError:
            return ''
    return wrapper


def get_html(url_to_get: str) -> str:
    return requests.get(url_to_get).text


def get_news(html: str) -> List[dict]:
    soup = Bs(html, 'lxml')

    @try_get
    def get_title(article: bs4.element.Tag) -> str:
        return clear_text(article.find(class_='ArticleItem--name').text)

    @try_get
    def get_img(article: bs4.element.Tag) -> str:
        return clear_text(article.find('img').attrs.get('src'))

    @try_get
    def get_link(article: bs4.element.Tag) -> str:
        return clear_text(article.find('a', class_='ArticleItem--name').attrs.get('href'))

    return [
        {'title': get_title(item), 'image': get_img(item), 'link': get_link(item)}
        for item in soup.find_all(class_='ArticleItem', limit=20)]


def get_description(html: str) -> List[str]:
    inserting_index = 0
    message_set = []
    soup = Bs(html, 'lxml')
    description = []
    for element in soup.find(class_='BbCode'):
        if not element.attrs.get('class') and element.name == 'p':
            description.append({
                'type': 'p',
                'text': element.text
            })
        elif element.name == 'h2':
            description.append({
                'type': 'h2',
                'text': element.text
            })
        elif element.attrs.get('class')[0] == 'bb-vrez':
            description.append({
                'type': 'vrez',
                'text': element.text
            })
    for i in description:
        if i['type'] in ['h2', 'vrez'] and len(message_set) != 0:
            inserting_index += 1

        try:
            message_set[inserting_index] += i['text']
        except IndexError:
            message_set.insert(inserting_index, i['text'] + '\n\n')

        last_inserted_type = i['type']

        if last_inserted_type == 'vrez':
            inserting_index += 1

    return message_set


if __name__ == '__main__':
    import datetime
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    url = f'https://kaktus.media/?lable=8&date={today}&order=time'
    news = get_news(get_html(url))

    for i in get_description(get_html('https://kaktus.media/doc/483316_syrrogatnoe_materinstvo_v_kyrgyzstane:_zapretit_ili_izmenit_ysloviia_mneniia_ekspertov.html')):
        print(i)
        print()

