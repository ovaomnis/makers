from typing import Callable
from data import cats, subcats, levels, currencies
import random

courses = {
    1: {
        'cat': '', 
        'subcat': '', 
        'title': '', 
        'body': '', 
        'level': '', 
        'price': {
            'currency': '',
            'amount': ''
        }
    },
}

index = len(courses)


def get_course(index: int, exception: bool = False):
    course = courses.get(index, None)
    
    if exception:
        if not course:
            raise Exception(f'No course with index: {index}')
    
    return course


def get_while_from_list(title: str, choices: list[str]):
    while True:
        print(f'\nPlease choose {title} (number): ')
        print('\n'.join([f'{i + 1}) {choices[i]}' for i in range(len(choices))]))
        try:
            choice = int(input(f'Enter number of {title}: '))
            if 1 <= choice <= len(choices):
                return choices[choice - 1]
            else:
                continue
        except ValueError:
            continue


def ask_till_valid(title: str, validator: Callable[[str], bool], msg: str) -> str:
    while True:
        inp = input(f'\nPlease enter {title}: ')
        if validator(inp):
            return inp
        else:
            print(msg)
            continue


def create_course(cat: str, subcat: str, title: str, body: str, level: str, currency: str, amount: int):
    global index
    index += 1
    courses.update({
            index: {
                'cat': cat,
                'subcat': subcat,
                'title': title,
                'body': body,
                'level': level,
                'price': {
                        'currency': currency,
                        'amount': amount 
                    },
            } 
        })


def change_body(index: int, body: str):
    course = get_course(index=index, exception=True)
    course['body'] = body
    courses.update({index: course})


def remove_course(index: int):
    try:
        courses.pop(index)
    except KeyError:
        raise KeyError(f"There is no course with index: {index}")


def start():
    cat = get_while_from_list('Категория', cats)
    subcat = get_while_from_list('Подкатегория', subcats)
    title = ask_till_valid('Заголовок курса', lambda x: True if 0 <= len(x) <= 60 else False, '(максимум 60 символов)')
    body = ask_till_valid('Описание к курсу', lambda x: True if 10 <= len(x.split()) else False, '(минимум 10 слов)')
    level = get_while_from_list('Уровень', levels)
    currency = get_while_from_list('валюта', currencies)
    amount = int(ask_till_valid('сумма', lambda x: True if x.isnumeric() else False, 'Enter number'))
    
    create_course(cat, subcat, title, body, level, currency, amount)
    