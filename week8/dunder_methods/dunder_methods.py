"""
Magic methods in Python (dunder -> double underscore)
"""

# Super methods
# Service methods

# methods which has 2 underscores in the beginning and in the ending. Magic is when we do not call straightly
# they called by specific methods and functions

# __str__, __init__

# __new__ -> class constructor. due to creating object
# __init__ -> initiator. initiating object. sets attrs to object
# __del__ -> destructor. due to destroying. called when object destroys


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('Methods __init__')
#
#     def __del__(self):
#         print('Instance deleted', self)
#
#
# a = Point(4, 4)
# b = Point(8, 2)


# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print('Method __new__ for class', cls)
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('Methods __init__')
#
#     # def __del__(self):
#     #     print('Instance deleted', self)
#
#
# a = Point(4, 4)
# b = Point(8, 2)


# class User:
#     def __new__(cls, name: str, age: int):
#         if age > 18:
#             return super().__new__(cls)
#         raise ValueError('You are too young')
#
#     def __init__(self, name: str, age: int):
#         self.name, self.age = name, age
#
#     def __str__(self):
#         return self.name
#
#     def __del__(self):
#         print('Bye')

# import datetime
# print(repr(datetime.date.today()))

# __str__ -> for easy reading
# __repr__ -> link to object in memory
# if str not defined, then str uses repr


# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other): +
#         return f'add result of: {self.value + other}'
#
#     def __sub__(self, other):
#         pass
#
#     def __floordiv__(self, other): //
#         pass
#
#     def __mod__(self, other): %
#         pass
#
#     def __pow__(self, power, modulo=None): **
#         pass
#
#     def __truediv__(self, other): /
#         pass
#
#     def __mul__(self, other): *
#         pass


# obj_int = MyNumber(7)
# print(obj_int + 9)

# __invert__ -> reverses iterable object (~)

# class Base:
#     def __init__(self, string: str):
#         self.string = string
#
#     def __invert__(self):
#         print('Invert')
#         return self.string[::-1]
#
#
# base = Base("Hello World")

# __hash__ -> hashing data
# hash()
# print(hash('hello'))

# __getattribute__(self, item) -> called when trying to get attribute of instance of class
# string = 'Hello'
# print(string.lower())
# print(string.__getattribute__('lower')())

# __getattr__ -> when trying to get not existing attribute
# __setattr__ -> called when setting attribute
# __delattr__ -> called when deleting attribute


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item: str):
        print('getattribute')
        if item == 'x':
            return 'x'
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print('attribute set')
        super().__setattr__(key, value)


a = Point(2, 3)
print(a)
