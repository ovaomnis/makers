"""
Encapsulation
"""
from typing import Tuple


# 1. Encapsulation as link


# class Phone:
#     def __init__(self, number):
#         self.number = number
#
#     def print_number(self):
#         print(f'my number: {self.number}')
#
#
# nokia = Phone('+996999999999')
# nokia.print_number()
# Linked behavior of object with its data


# 2. Encapsulation as hiding data of class (manage access)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# pt = Point(5, 7)
# print(pt, pt.x, pt.y)

# pt.x = 8
# pt.y = 'coder y'
# print(pt, pt.x, pt.y)

# 3 access modification
# 1. public -> public access (without underscore) -> able to use for everyone x, y, number

# 2. _protected -> protected attr (with one underscore) -> data can be changed or red in class or child classes
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
# print(pt, pt._x, pt._y)


# 3. __private -> able to use only in classes
# class Point:
#     def __init__(self, x, y) -> None:
#         self.__x = x
#         self.__y = y
#
#     def get_coords(self) -> Tuple[int | float, int | float]:
#         return self.__x, self.__y
#
#     def set_coord(self, new_x: int, new_y: int) -> None:
#         if isinstance(new_x, (int, float)) and isinstance(new_y, (int, float)):
#             self.__x = new_x
#             self.__y = new_y
#         else:
#             raise TypeError('Coords have to be int or float')
#
#
# pt = Point(2, 2)
# # print(pt, pt._Point__x, pt._Point__y)
# pt.set_coord(4, 4)
# print(pt.get_coords())


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self._age = age
#
#     def get_age(self) -> int:
#         return self._age
#
#     def set_age(self, age: int) -> None:
#         if not isinstance(age, (int, float)):
#             raise TypeError("Age have to be in (int, float) type")
#         self._age = age
#
#     def __str__(self):
#         return f'Name: {self.name}, age: {self._age}'
#
#
# p1 = Person('Ronald', 21)
# print(p1)
# print(p1.get_age())
# p1.set_age(18)
# print(p1.get_age())


# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('age can be only int/float')
#         if not(0 < value < 110):
#             raise ValueError('invalid age')
#         self._age = value
#
#
# a = Person('Kate', 43)
# a.age = 109
# print(a.age)


class Russia:
    __name = 'Russian Federation'
    __population = 0

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError('Population have to be int/float and greater than 0')
        self.__population = value


russia = Russia()
russia.population = 0
print(russia.population)





