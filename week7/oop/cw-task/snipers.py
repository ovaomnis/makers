import random
import time
from typing import List


class Sniper:
    health: int

    def __init__(self, name):
        self.name = name
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def __str__(self):
        return self.name


class Fight:
    DAMAGE = 20
    out_of_game: List[Sniper] = []
    snipers: List[Sniper]

    def __init__(self, snipers: List[Sniper]):
        self.snipers = snipers

    def get_random_victim(self) -> Sniper | None:
        if len(self.snipers) == 1:
            return None
        return self.snipers.pop(self.snipers.index(random.choice(self.snipers)))

    def shoot(self, shooter: Sniper, victim: Sniper):
        victim.hit(self.DAMAGE)
        print(f'Sniper {shooter} made hit to {victim}, its health {victim.health}')
        if not victim.health:
            print(f'Sniper {victim} out of game')
            self.out_of_game.append(victim)
        else:
            self.snipers.append(victim)

    def game_over(self):
        print(f'Winner: {self.snipers[0]}')

    def start(self):
        victim = self.get_random_victim()

        if victim and len(self.snipers):
            self.shoot(random.choice(self.snipers), victim)
            # time.sleep(2)
            self.start()
        else:
            self.game_over()


fight = Fight(snipers=[
    Sniper('Sam'),
    Sniper('Raul'),
    Sniper('Ran')
])

fight.start()
