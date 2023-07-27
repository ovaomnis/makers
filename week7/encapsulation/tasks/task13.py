
class Game:
    __level = 0

    @property
    def level(self) -> int:
        return self.__level


game = Game()
print(game.level)

