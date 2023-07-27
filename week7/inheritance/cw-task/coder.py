from typing import List, Dict


class Coder:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.experience = 0
        self.count_code_time = 0

    def get_info(self) -> Dict:
        return {
            'name': self.name,
            'age': self.age,
            'experience': self.experience,
            'count_code_time': self.count_code_time
        }

    def coding(self, time):
        self.count_code_time += time


class Backend(Coder):
    def __init__(self, name: str, age: int, languages_backend: List[str]):
        Coder.__init__(self, name, age)
        self.languages_backend = languages_backend

    def get_info(self):
        info = super().get_info()
        info.update({
            'languages_frontend': self.languages_backend
        })
        return info



class Frontend(Coder):
    def __init__(self, name: str, age: int, languages_frontend: List[str]):
        Coder.__init__(self, name, age)
        self.languages_frontend = languages_frontend

    def get_info(self):
        info = super().get_info()
        info.update({
            'languages_frontend': self.languages_frontend
        })
        return info


class FullStack(Backend, Frontend):
    def __init__(self, name: str, age: int, languages_backend: List[str], languages_frontend: List[str]):
        Backend.__init__(self, name, age, languages_backend)
        Frontend.__init__(self, name, age, languages_frontend)


backend = Backend('john', 22, ['python'])
front = Frontend('jsne', 20, ['js'])


fs = FullStack(name='Ralph', age=21, languages_backend=['python'], languages_frontend=['javascript'])
print(fs.get_info())

