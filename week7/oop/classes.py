"""
introducing to OOP
"""
"""
OOP - programming paradigm, which based on concepts: Class and Object
"""
# Paradigm -> package of rules, ideas, concepts, which defines code writing style

"""
Class -> blueprint, description of which properties of behavior have object
"""
# properties - simple variables
# behavior - simple functions (methods)

"""
Object -> instance of class
"""

"""Syntax"""

# class <ClassName>: -> defined class
#     string = '' -> created variable or attribute or property
#
#     def some_method(self): -> created behavior or method or function in object
#         pass


# class A:
#     string = 'This is class A'
#
#     def __str__(self):
#         return self.string
#
#
# a = A()
#
# print(a)


class Person:
    legs = 2,
    arms = 2

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


print(dir(Person))
sam = Person('sam', 21)
print(dir(sam))

