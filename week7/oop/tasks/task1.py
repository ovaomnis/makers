class Song:
    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    def show_title(self):
        return f'Название этой песни {self.title}'

    def show_author(self):
        return f'Автор этой песни {self.author}'

    def show_year(self):
        return f'Эта песня вышла в {self.year} году'


song = Song('Pharrell Williams', 'Happy', 2013)
print(song.show_title())
print(song.show_author())
print(song.show_year())
