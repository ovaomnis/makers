
class Game:
    __level = 0

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, value: int) -> None:
        self.__level = value


game = Game()
print(game.level)
game.level = 10
print(game.level)



