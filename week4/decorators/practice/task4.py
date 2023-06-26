def benchmark(func):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        func(*args, **kwargs)
        print(f'Время выполнения: {round(time() - start, 2)} секунд.')
    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')
    return webpage.text


fetch_webpage()


