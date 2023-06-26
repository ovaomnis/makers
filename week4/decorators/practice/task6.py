
def is_admin(func):
    def wrapper(*args, **kwargs):
        user = func(*args, **kwargs)
        if user.get('is_admin'):
            print(f'Доступ разрешен {user.get("username", "")}')
        else:
            print(f'Доступ запрещен {user.get("is_admin", "")}')
    return wrapper


@is_admin
def get_user(dict_: dict) -> dict:
    return dict_


get_user({'username': 'john133', 'is_admin': True})
get_user({'username': 'jane133', 'is_admin': False})
