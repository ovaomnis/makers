"""
Multiple inheritance
"""

# isinstance() -> checks if class is example instance of other class
# issubclass() -> checks if class is subclass
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(B):
#     pass
#
#
# a = A()
# b = B()
# c = C()

# print(issubclass(C, A))
# print(isinstance(c, A))


# class User:
#     def __init__(self, username: str, age: int, city: str, password: str):
#         self.username = username
#         self.age = age
#         self.city = city
#         self.password = password
#
#     def get_profile_info(self):
#         return f'username: {self.username}\nage: {self.age}\ncity: {self.city}'
#
#     def greet_user(self):
#         return f'Welcome {self.username}!'
#
#
# class Admin(User):
#     def __init__(self, privileges, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.privileges = privileges


# class Lion:
#     color = 'black'
#
#
# class Lioness:
#     color = 'brown'
#
#
# class Child(Lioness, Lion):
#     pass
#
#
# obj = Child()
# print(obj.color)
# print(Child.__mro__)


"""
Multiple inheritance issues
"""

# 1. Romb issue -> fixed by mro

#    A
#    ^
#   / \
#  /   \
# B     C
# ^     ^
#  \   /
#   \ /
#    D

# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B, C):
#     pass
#
#
# print(D.mro())


# class X:
#     pass
#
#
# class Y:
#     pass
#
#
# class Z:
#     pass
#
#
# class A(X, Y):
#     pass
#
#
# class B(Y, Z):
#     pass
#
#
# class M(B, A, Z):
#     pass


# print(M.mro())


# 2. Cross issue (not solved)


# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C(A, B):
#     pass
#
#
# class D(B, A):
#     pass
#
#
# class M(C, D):
#     pass
#
#
# print(M.mro())


"""
Mixins -> inheriting classes
"""

# used to be inherited to create new class by mixin classes

# How to work with mixins
# 1. Convenient to name mixin classes with Ending like Mixin: CreateMixin, SetListMixin
# 2. They are not used to create other instances
# 3. Used to expand functionality of class


# class MoveMixin:
#     def move(self):
#         print('I am moving')
#
#
# class StopMixin:
#     def stop(self):
#         print('I am standing')
#
#
# class Car(MoveMixin, StopMixin):
#     pass
#
#
# class Person(MoveMixin, StopMixin):
#     pass
#
#
# car = Car()
# person = Person()
#
# car.move()
# car.stop()
# person.move()
# person.stop()


# class InitTodos:
#     def __init__(self):
#         self.todos = {}
#
#
# class CreateMixin(InitTodos):
#     def create(self, todo, key):
#         if key in self.todos:
#             return 'Todo already exists'
#         self.todos[key] = todo
#         return self.todos
#
#
# class DeleteMixin(InitTodos):
#     def delete(self, key):
#         return self.todos.pop(key)
#
#
# class UpdateMixin(InitTodos):
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos[key]
#
#
# class ReadMixin(InitTodos):
#     def read(self):
#         return sorted(self.todos.items())
#
#
# class Note(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     def __init__(self):
#         super().__init__()
#
#
# tasks = Note()
# tasks.create('Hello', 1)
# tasks.create('H/W', 2)
# tasks.delete(1)
# tasks.update(2, 'Done')
# print(tasks.read())

# print(tasks.todos)

