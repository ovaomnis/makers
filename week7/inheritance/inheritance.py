""" Inheritance """

# Main concepts of OOP: Inheritance, Polymorphism, Encapsulation

# Other concepts: Association, Aggregation, Composition, Abstraction

'''
Inheriting syntax
'''


# class Parent:
#     Methods and Attributes of parents class

# class Child_class(Parent_class):
#     Methods and Attributes of parents class

''''
Inheritance - concept of OOP, which says that we can Inherit, override or use methods and attributes
of parent class in child class. Creating new class based on Existing class
'''


# class A:
#     def func1(self, a):
#         print(self, a)
#
#     def __str__(self):
#         return 'This is object of class A'
#
#
# class B(A):
#     def __str__(self):
#         return "This is object of class B"
#
#
# b1 = B()
# a1 = A()
# b1.func1(2)

# 0

'''
MRO - method resolution order
order of searching attributes
'''


# class A:
#     x = 'x in A'
#     y = 'y in '
#
#
# class B(A):
#     x = 'x in B'
#
#
# a = A()
# b = B()

# print(b.x)
# print(b.y)
#
# print(a.x)
# print(a.y)

# print(B.mro()) # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# print(B.__mro__) # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        print(self.name)
        print(self.last_name)
        print(self.age)


class Student(Person):
    def __init__(self, group, faculty, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group = group
        self.faculty = faculty

    def get_info(self):
        super().get_info()
        print(self.group)
        print(self.faculty)


s1 = Student('Math21', 'AppMath&Informatics', name='Adil', last_name='Ibraliev', age=21)
s1.get_info()

b