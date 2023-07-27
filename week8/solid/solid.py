from typing import List


# S -> single responsibility principle SRP
# O -> open-closed principle (expend not change) OCP
# L -> Liskov substitution principle LSP
# I -> interface segregation principle ISP
# D -> dependency inversion principle DIP


# user_data = [
#     {
#         'name': 'Sam',
#         'surname': 'Brown',
#         'profession': 'detective'
#     },
#     {
#         'name': 'John',
#         'surname': 'Sean',
#         'profession': 'wrestler'
#     }
# ]
# SRP wrong
# class ExportCSV:
#     def __init__(self, data):
#         self.data = self.prepare(data)
#
#     def prepare(self, data: List[dict]):
#         resul = ''
#         for item in data:
#             new_line = ','.join(item.values())
#             resul += new_line + '\n'
#         return resul
#
#     def write_file(self, filename):
#         with open(filename, 'w') as file:
#             file.write(self.data)

# SRP correct
# class FormatData:
#     def __init__(self, data: List[dict]):
#         self.data = data
#
#     def prepare(self):
#         resul = ''
#         for item in self.data:
#             new_line = ','.join(item.values())
#             resul += new_line + '\n'
#         return resul
#
#
# class ExportCSV:
#     def __init__(self, filename: str):
#         self.filename = filename
#
#     def write_file(self, data: str):
#         with open(self.filename, 'w') as file:
#             file.write(data)
#
#
# prepared_data = FormatData(user_data).prepare()
# ex = ExportCSV('data.csv')
# ex.write_file(prepared_data)

# OCP correct
# import time
#
#
# class Logger:
#     def __init__(self):
#         self.format = '%Y:%m:%d %H:%M:%S'
#
#     def log(self, message):
#         curr_time = time.localtime()
#         print(time.strftime(self.format, curr_time))
#
#
# class CustomLogger(Logger):
#     def __init__(self):
#         super().__init__()
#         self.format = '%Y:%m:%d'
#
#
# log = CustomLogger()
# log.log('Hello')

# OCP wrong
# from enum import Enum
#
#
# class Product(Enum):
#     SHIRT = 1
#     PANT = 2
#     TSHIRT = 3


# class DiscountCalculator:
#     def __init__(self, product_type, cost):
#         self.product_type = product_type
#         self.cost = cost
#
#     def get_discount_price(self):
#         if self.product_type == Product.SHIRT:
#             return self.cost - (self.cost*.1)
#         elif self.product_type == Product.TSHIRT:
#             return self.cost - (self.cost*.15)
#         elif self.product_type == Product.PANT:
#             return self.cost - (self.cost*.20)

# OCP correct
# from abc import ABC, abstractmethod
#
#
# class DiscountCalculator(ABC):
#     @abstractmethod
#     def get_discount_price(self):
#         pass
#
#
# class DiscountCalcShirt(DiscountCalculator):
#     def __init__(self, cost):
#         self.cost = cost
#
#     def get_discount_price(self):
#         return self.cost - self.cost*.10
#
#
# class DiscountCalcTshirt(DiscountCalculator):
#     def __init__(self, cost):
#         self.cost = cost
#
#     def get_discount_price(self):
#         return self.cost - self.cost * .15
#
#
# class DiscountCalcPants(DiscountCalculator):
#     def __init__(self, cost):
#         self.cost = cost
#
#     def get_discount_price(self):
#         return self.cost - self.cost * .20


# LSP wrong
# class Animal:
#     def __init__(self, attrs):
#         self.attributes = attrs
#
#     def eat(self, *args):
#         print('Ate some food')
#
#
# class Cat(Animal):
#     def eat(self, amount):
#         if amount > 300:
#             print('Too much')
#         else:
#             print('Ate some cat food')
#
#
# class Dog(Animal):
#     def eat(self, *args):
#         print("Ate some dog food")


# LSP correct
# class Animal:
#
#     def __init__(self, name: str, age: int) -> None:
#         self.attributes = {
#             'name': name,
#             'age': age
#         }
#
#     def eat(self, _amount=0):
#         print('Eating')
#
#
# class Cat(Animal):
#
#     def __init__(self, name: str, age: int) -> None:
#         super().__init__(name, age)
#
#     def eat(self, _amount=0):
#         if _amount > 300:
#             print("TOO MUCH")
#         else:
#             print("Eating")
#
#
# class Dog(Animal):
#
#     def __init__(self, name: str, age: int) -> None:
#         super().__init__(name, age)
#
#     def eat(self, _amount=0):
#         print("Eating")
#
#
# cat1 = Cat('Barsik', 12)
# cat2 = Cat('Mursik', 7)
# dog = Dog('Muhtar', 10)
#
# for i in [cat2, cat1, dog]:
#     print(i.attributes['name'])


# ISP wrong
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#     def swim(self):
#         pass
#
#     def walk(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def talk(self):
#         pass
#
#
# class Human(Creature):
#     def swim(self):
#         print('i can swim')
#
#     def walk(self):
#         print('i can walk')
#
#     def talk(self):
#         print('i can talk')
#
#
# class Fish(Creature):
#     def swim(self):
#         print('i can swim')
#
#     def fly(self):
#         print('i cant fly')
#
#
# fish = Fish('trout')
# fish.talk()
# fish.walk()

# ISP correct:
# class Creature:
#     def __init__(self, name):
#         self.name = name
# 
# 
# class Swimmer:
#     def swim(self):
#         pass
# 
# 
# class Walker:
#     def walk(self):
#         pass
#     
#     def run(self):
#         pass
# 
# 
# class Flying:
#     def fly(self):
#         pass
# 
# 
# class Talker:
#     def talk(self):
#         pass
#     
#     def scream(self):
#         pass
# 
# 
# class Human(Creature, Walker, Talker):
#     ...


# DIP wrong

