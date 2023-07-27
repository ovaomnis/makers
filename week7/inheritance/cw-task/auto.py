class Auto:
    def ride(self):
        print('Riding on a ground')


class Boat:
    def swim(self):
        print('floating on water')


class Amphibian(Auto, Boat):
    pass


amph = Amphibian()
amph.swim()
amph.ride()
