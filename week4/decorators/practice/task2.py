from datetime import datetime


def func_start_time(func):
    def wrapper(*args, **kwargs):
        print(f'Функция запущена {datetime.now().strftime("%d.%m.%y %H:%M")}')
        func()
    return wrapper


@func_start_time
def func():
    print('Hello world')


func()
