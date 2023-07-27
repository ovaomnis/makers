class Game:
    __level = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def play(self, hours: int) -> None:
        if isinstance(hours, int) and hours > 2:
            self.__level += 1

    def get_level(self) -> int:
        return self.__level


game = Game('Mulan')
print(game.get_level())
game.play(2)
game.play(3)
print(game.get_level())
