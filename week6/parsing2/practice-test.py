import requests
from bs4 import BeautifulSoup
import csv

"""
1)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""
# with open('vestidata.csv', 'w') as file:
#     write_ = csv.writer(file)
#     write_.writerow(['title'])
#
# res = requests.get('https://vesti.kg')
# soup = BeautifulSoup(res.text, 'lxml')
#
# for news in soup.find(attrs={'id': 'itemListLeading'}).find_all('a'):
#     title = news.text.replace('\n', '').strip()
#     with open('vestidata.csv', 'a') as file:
#         write_ = csv.writer(file)
#         write_.writerow([title])

"""
2)	EXTRA: Спарсить https://www.kinopoisk.ru/lists/movies/top250/ и записать результат в csv файл
"""
with open('kinopoisk.csv', 'w') as file:
    write_ = csv.writer(file)
    write_.writerow(['title'])

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0, win64; x64) AppleWebKit/537.36 (KHTML., like Gecko) Chrome/68.0.3029.10 Safari/537.3"}
res = requests.get('https://www.kinopoisk.ru/lists/movies/top250/', headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

print(soup)

