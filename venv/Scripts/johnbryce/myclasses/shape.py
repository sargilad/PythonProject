import math


class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Ellipse:
    radius: int

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)


class Circle(Ellipse):
    pass
