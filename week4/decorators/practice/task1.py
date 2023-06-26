from typing import Callable


def call_function(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Вызываю функцию {func.__name__}')
        func()
        print(f'Вызов функции {func.__name__} прошёл успешно')
    return wrapper


@call_function
def first():
    print("hello world")
    return "hello world"


first()

