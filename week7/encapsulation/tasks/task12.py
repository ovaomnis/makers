
class Game:
    __level = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def set_level(self, level):
        self.__level = level

    def get_level(self) -> int:
        return self.__level


game = Game('Raychel')
game.set_level(10)
print(game.get_level())

