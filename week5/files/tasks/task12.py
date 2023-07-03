from typing import List


def bad_students(filename: str) -> List[str]:
    with open(filename) as file:
        students = [s.replace('\n', '').split() for s in file.readlines()]
    return [student[1] for student in students if int(student[2]) < 4]