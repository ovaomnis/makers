import datetime


def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called at: {datetime.datetime.now()} with args: {args} and kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper