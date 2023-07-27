class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def display(self):
        print(f"name:{self.name}, age:{self.age}")


class Student(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty

    def display_student(self):
        print(f"name:{self.name}, age:{self.age}, faculty:{self.faculty}")


obj_student = Student('science', 'Rick', 21)
obj_student.display()
obj_student.display_student()


