class MyString(str):
    def __init__(self, value: str):
        self.value = value

    def append(self, letter: str):
        self.value += letter

    def pop(self):
        last = self.value[-1]
        self.value = self.value[:-1]
        return last

    def __str__(self):
        return self.value


example = MyString('String')
example.append('hello')
print(example.pop())
print(example)
