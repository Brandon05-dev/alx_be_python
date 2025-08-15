# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Base method to calculate area; must be overridden in derived classes"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate rectangle area"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Override area method to calculate circle area"""
        return math.pi * self.radius ** 2
