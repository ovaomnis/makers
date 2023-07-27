class RadioMixin:
    def play_music(self, music: str):
        print(f'Playing {music}')


class Auto(RadioMixin):
    def ride(self):
        print('Riding on a ground')


class Boat(RadioMixin):
    def swim(self):
        print('floating on water')


class Amphibian(Auto, Boat):
    pass


amph = Amphibian()
amph.swim()
amph.ride()
amph.play_music('Disfruto')

