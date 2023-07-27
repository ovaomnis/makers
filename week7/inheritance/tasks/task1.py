class Class1:
    def first(self):
        print('First')

    def second(self):
        print('Second')


class Class2(Class1):
    def third(self):
        print('Third')

    def fourth(self):
        print('Fourth')


obj = Class2()
print(obj.first())
print(obj.second())
print(obj.third())
print(obj.fourth())
