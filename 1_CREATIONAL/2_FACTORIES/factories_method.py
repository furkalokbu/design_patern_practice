from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


    class PointFactory:

        @staticmethod
        def new_cartesian_point(x, y):
            point = Point()
            point.x = x
            point.y = y
            return point

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()

if __name__ == '__main__':
    p1 = Point(2,3)
    p2 = Point.factory.new_cartesian_point(2,3)
    p3 = Point.factory.new_polar_point(1,3)
    print(p1, p2, p3)
