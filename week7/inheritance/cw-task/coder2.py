from typing import List, Dict


class Coder:
    experience = 0
    count_code_time = 0

    def get_info(self) -> Dict:
        return {
            'experience': self.experience,
            'count_code_time': self.count_code_time
        }

    def coding(self, amount: int):
        self.count_code_time += amount


class Backend(Coder):
    def __init__(self, languages_backend: List[str]):
        self.languages_backend = languages_backend

    def get_info(self):
        info = super().get_info()
        info.update({
            'language_backend': self.languages_backend
        })
        return info


class Frontend(Coder):
    def __init__(self, languages_frontend: List[str]):
        self.languages_frontend = languages_frontend

    def get_info(self):
        info = super().get_info()
        info.update({
            'languages_frontend': self.languages_frontend
        })
        return info


class Fullstack(Backend, Frontend):
    def __init__(self, languages_backend: List[str], languages_frontend: List[str]):
        Backend.__init__(self, languages_backend)
        Frontend.__init__(self, languages_frontend)

    def get_info(self):
        info = super().get_info()
        info.update(Frontend.get_info(self))
        return info


back = Backend(['Python', 'Rust', 'Go', 'Node'])
front = Backend(['JavaScript', 'Flutter', 'Kotlin', 'Swift', 'HTML', "CSS", 'Node'])
fullstack = Fullstack(['Python', 'Rust', 'Go', 'Node'],['JavaScript', 'Flutter', 'Kotlin', 'Swift', 'HTML', "CSS", 'Node'])

print(back.get_info())
print(front.get_info())
print(fullstack.get_info())

