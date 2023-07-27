import random


class Language:
    students = 0

    def __init__(self, name):
        self.name = name

    def increment_student(self):
        self.students += 1


class Languages:
    langs = {
        'JavaScript': Language("JavaScript"),
        'Python': Language("Python")
    }
    all_students = 0
    base_lang = langs['Python']

    def update_student_count(self):
        self.all_students = self.langs['JavaScript'].students + self.langs['Python'].students

    def coding(self):
        return f'I amd {self.base_lang.name} student. I am coding now'


class Python(Languages):
    def __init__(self):
        super().langs['Python'].increment_student()
        super().update_student_count()


class JavaScript(Languages):
    def __init__(self):
        self.base_lang = self.langs['JavaScript']
        super().langs['JavaScript'].increment_student()
        super().update_student_count()


py = (Python(), Python(), Python(), Python(), Python(), Python())
js = (JavaScript(), JavaScript(), JavaScript(), JavaScript(), JavaScript())


random_student = random.choice(py + js)
while True:
    print('I have selected Student. Guess who is it (Python/JavaScript):')
    guess = ''.join(input().strip().split()).lower()
    print(guess)
    if random_student.base_lang.name.lower() == guess:
        print('Good job!')
        break
    else:
        print('No bueno :(')
        print('Try again:')
