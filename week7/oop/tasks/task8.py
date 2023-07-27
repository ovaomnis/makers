from typing import Callable
import re


class Validator:
    def __init__(self, fc: Callable[[str], bool], err_msg=''):
        self.validate = fc
        self.err_msg = err_msg


class Password:
    validators = [
        Validator(lambda x: 8 <= len(x) <= 15, 'Password should be longer than 8, and less than 15'),
        Validator(lambda x: bool(re.match(r'\d', x)), 'Password should contain numbers too'),
        Validator(lambda x: bool(re.match(r'\w', x)), 'Password should contain letters as well'),
        Validator(lambda x: bool(re.compile(r"[@#&$%!~*]").search(x)), 'Your password should have some symbols')
    ]

    def __init__(self, password: str):
        self.password = password
        if all(map(lambda validator: self.validate(validator.validate(self.password), validator.err_msg), self.validators)):
            print('Ваш пароль сохранен.')

    def validate(self, valid: bool, msg: str):
        if valid:
            return True
        else:
            print(msg)
            return False

    def __str__(self):
        return '*'*len(self.password)


p1 = Password('1helloworld$')
print(p1)
