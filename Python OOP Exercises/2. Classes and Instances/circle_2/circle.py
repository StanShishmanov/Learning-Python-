# from math import pi

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        result = 3.14 * (self.radius ** 2)
        return round(result, 2)

    def get_circumference(self):
        result = 2 * 3.14 * self.radius
        return round(result, 2)


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
