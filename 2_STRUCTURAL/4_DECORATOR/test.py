from abc import ABC
from unittest import TestCase
import unittest


class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return f'A circle of radius {self.radius}'

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return f'A {self.shape} of side {self.side}'


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    r = getattr(self.shape, 'resize', None)
    if callable(r):
        self.shape.resize(factor)

  def __str__(self):
    return f'{self.shape} has the color {self.color}'

class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual('A circle of radius 5 has the color red',
                         str(circle))
        circle.resize(2)
        self.assertEqual('A circle of radius 10 has the color red',
                         str(circle))

if __name__ == '__main__':
    unittest.main()
    # circle = ColoredShape(Circle(5), 'red')
    # print(circle)
