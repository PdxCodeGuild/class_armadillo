"""
just a test module for demonstrating classes and docstrings
"""

import math


class Point:
    """
    a 2D point with floats
    """

    def __init__(self, x, y):
        """
        point initializer
        :param x: the x value of the point
        :param y: the y value of the point
        """
        self.x = x
        self.y = y

    def distance(self, p):  # method, or 'member function'
        """
        calculate the distance between two points
        :param p: the point to which we'll calculate the distance
        :return: the distance between the two points
        """
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)

    def scale(self, v):
        """
        scales a point
        :param v: the value to scale by
        :return: nothing
        """
        self.x *= v
        self.y *= v

    def __str__(self):
        """
        :return: the human-readable string representation of this object 
        """
        return f'[{self.x},{self.y}]'


def add(a, b):
    """
    adds two numbers and returns the result
    :param a: the first number to be added
    :param b: the second number to be added
    :return: the sum of the first and second number
    """

    return a + b