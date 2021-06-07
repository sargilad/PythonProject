import math

from abc import *


# abstract class
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Ellipse(Shape):
    def get_perimeter(self, a, b):
        return a + b

    radius: int

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)


class Circle(Ellipse):
    pass
