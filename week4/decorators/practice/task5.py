users = {
    'vasya': 'hellokitty',
    'alesha': 'alesha1234'
}


def validate_password(func):
    def wrapper(username: str, password: str):
        user = users.get(username, None)
        if user:
            if user != password:
                print('Password is invalid')
                return 0
        else:
            print('Username is not defined')
            return 0
        func(username, password)
    return wrapper


@validate_password
def login(username: str, password: str):
    print(f'Welcome, {username}')


login('alesha', 'alesha1234')

