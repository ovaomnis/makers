
class Game:
    __level = 0

    def __init__(self, name: str) -> None:
        self.__validate_name(name)

    def __validate_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError(f'Name, not a {type(name)}. You idiot !')
        self.name = name.title()

    def set_level(self, level):
        if self.name == 'Tolik':
            self.__level = level
        else:
            print(f'{self.name} ты не Tolik!')


game = Game('Raychel')
game.set_level(5)
print(game._Game__level)

game2 = Game("TOLIK")
game2.set_level(5)
print(game2._Game__level)
