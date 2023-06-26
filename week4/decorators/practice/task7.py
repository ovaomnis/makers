def route(func):
    def wrapper(path: str):
        return f'https://www.mywebsite.com/{path}'
    return wrapper


@route
def get_page(path):
    return path


print(get_page('about/'))
print(get_page('products/'))