def repeat(times: int):
    def decor(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decor


@repeat(20)
def print_hello():
    print('Hello World')


print_hello()
