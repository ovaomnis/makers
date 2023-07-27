"""
Instance methods, class methods, static methods
"""

# 1.instance methods
# 2.Class methods
# 3.Static methods

# Instance methods is simple methods, which takes as first arg self (link to object). Used to work with object attrs


# class A:
#     def instance_method(self):
#         print("Instance methods")
#         print("First argument", self)
#
#
# a = A()
# a.instance_method()
# A.instance_method(a)


# 2. Class methods
'''
class method = method, which takes as first argument link to class (cls)
Used to create objects or change class attrs. To create class methods, we have to decorate with @classmethod
'''


# class B:
#     @classmethod
#     def class_method(cls):
#         print('Class method')
#         print('First argument,', cls)
#
#
# B.class_method()
# obj = B()
# obj.class_method()


class Pizza:
    def __init__(self, radius, *ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def cook(self):
        print(f'A {self.radius}sm pizza is being prepared with ingredients: {", ".join(self.ingredients)}')

    @classmethod
    def four_cheese(cls, r):
        pizza = cls(r, 'Mozzarella', 'Cheddar', 'Holland cheese', 'Dor blue')
        return pizza


pizza1 = Pizza(45, 'Pepperoni', 'Ananas', 'Chili', 'Olives')
pizza_4_cheese = Pizza.four_cheese(35)
pizza_4_cheese.cook()
