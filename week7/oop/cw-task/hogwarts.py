import random
from typing import List


class Faculty:
    def __init__(self, name: str, quality: str):
        self.name = name
        self.quality = quality
        self.grade = None

    def detect_quality(self, exclude: List[int]):
        self.grade = random.choice([i for i in range(1, 101) if i not in exclude])

    def __str__(self):
        return self.name


class Hogwarts:
    def __init__(self):
        self.faculties = [
            Faculty('Gryffindor', 'courage'),
            Faculty('Ravenclaw', 'intelligence'),
            Faculty('Hufflepuff', 'justice'),
            Faculty('Slytherin', 'ambition')
        ]
        self.faculty = None

    def sorting_hat(self):
        for faculty in self.faculties:
            faculty.detect_quality([f.grade for f in filter(lambda x: x, self.faculties)])

        self.faculty = max(self.faculties, key=lambda x: x.grade)


class Student(Hogwarts):
    def __init__(self, first_name: str, last_name: str):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.detect_faculty()

    def detect_faculty(self):
        if not(self.first_name.lower() == 'harry' and self.last_name.lower() == 'potter'):
            self.sorting_hat()
        else:
            self.faculty = self.faculties[0]
        print(f'Преобладает {self.faculty.quality} -> {self.faculty}')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


s1 = Student('Harry', "Potter")
