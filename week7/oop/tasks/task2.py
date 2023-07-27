class Circle:
    pi = 3.14
    color = 'Синий'

    def __init__(self, radius, color='синий'):
        self.color = color
        self.radius = radius

    def get_area(self):
        return self.pi * self.radius**2


circle = Circle(2)
print(f'{circle.color}\n{circle.get_area()}')
