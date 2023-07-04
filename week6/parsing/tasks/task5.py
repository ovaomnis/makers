from typing import List

import requests
from bs4 import BeautifulSoup as Bs


res = requests.get('https://enter.kg/')
soup = Bs(res.text, 'lxml')
category_list = []

for i in soup.find_all('li', class_='VmClose'):
    if not i.text.isspace():
        category_list.append({
            'name': i.find('a').text,
            'link': 'https://enter.kg' + i.find('a').attrs.get('href')
        })


def find_category(category_list: List, keyword: str):
    cat = None
    sub_cats = []
    for cat in category_list:
        if cat['name'].lower().count(keyword.lower()):
            cat = cat
            break

    if not cat:
        return sub_cats

    response = requests.get(cat['link'])
    cat_soup = Bs(response.text, 'lxml')
    return [sub_cat.text for sub_cat in cat_soup.find_all('span', class_='category-product-count')]


print(find_category(category_list, 'Ноутбуки'))
