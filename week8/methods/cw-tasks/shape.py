class Shape:
    @staticmethod
    def get_circle_area(radius: int):
        return 3.1459265359 * radius**2


print(Shape.get_circle_area(30))
