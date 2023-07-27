from abc import ABC, abstractmethod
from enum import Enum, auto


class CarType(Enum):
    SEDAN = auto()
    CROSSOVER = auto()
    OFF_ROAD = auto()

    def __str__(self):
        return self.name.capitalize()


class Car(ABC):
    car_type: CarType
    millage: int
    price: int

    @abstractmethod
    def get_info(self):
        ...


class Toyota(Car):
    def __init__(self, millage: int, price: int, car_type: CarType):
        self.type = car_type
        self.millage = millage
        self.price = price

    def get_info(self):
        return f'Car Type: {self.type}, Millage: {self.millage}km, Price: {self.price}$'


toyota = Toyota(millage=12300, price=17900, car_type=CarType.SEDAN)
print(toyota.get_info())
