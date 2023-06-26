'''CRUD'''

db = [
    {'username': 'Hello', 'password': hash('12345test')},
    {'username': 'JhonSnow', 'password': hash('12345678')}
]

# GETTING USER LOGIC
def password_check(user: dict, password: str):
    if user['password'] != hash(password):
        raise Exception('Passwords does not match')
    

def get_user(username: str, exists=False):
    for user in db:
        if user['username'] == username:
            if exists:
                raise Exception('User already Exists')
            return user
        
    if not exists:        
        raise Exception('No such user in Database')


# REGISTER LOGIC
def register(username: str, passwrod: str, password_confirm: str):
    user = get_user(username, exists=True)

    if passwrod != password_confirm:
        raise Exception('Passwords is not match')

    db.append({'username': username, 'password': hash(passwrod)})
    return 'You successfuly registered !'

register('Adil', '1234asdf', '1234asdf')


# LOGIN LOGIC
def login(username: str, password: str):
    user = get_user(username)
    password_check(user, password)

    return('You successfuly logined')

login('Adil', '1234asdf')


# PASSWORD CHANGE
def change_password(username: str, old_passord:str, password: str, password_confirm: str):
    user = get_user(username)
    if user['password'] != hash(old_passord):
        raise Exception('Old password does not match')
    
    password_check(user, old_passord)
    
    user['password'] = hash(password)
    return 'Password successfuly changed'

change_password('Adil', '1234asdf', 'new_pass', 'new_pass')


# DELETE USER
def delete_account(username: str, password: str):
    user = get_user(username)
    password_check(user, password)

    db.remove(user)

delete_account('Adil', 'new_pass')

print(db)