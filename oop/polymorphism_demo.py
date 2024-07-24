"""
Objective: Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

Task Description:
You are tasked with creating a Python script named polymorphism_demo.py. In this script, define a base class Shape with a method area()
and derived classes Rectangle and Circle, each overriding the area() method to calculate their respective areas.

polymorphism_demo.py:
Base Class - Shape:

Method: area(self), which simply raises a NotImplementedError, indicating that derived classes need to override this method.
Derived Class - Rectangle:

Inherits from Shape.
Attributes: length and width.
Overrides the area() method to calculate the rectangle’s area using the formula: length × width.
Derived Class - Circle:

Inherits from Shape.
Attributes: radius.
Overrides the area() method to calculate the circle’s area using the formula: π × radius² (use math.pi for π).
main.py (Provided for Testing):
This script demonstrates polymorphism by creating instances of Rectangle and Circle, invoking their area() method, and showing that each class calculates the area according to its shape.

Expected Output:
When you run main.py, the output should reflect the areas of the different shapes, showcasing polymorphism through method overriding.

The area of the Rectangle is: 50
The area of the Circle is: 153.93804002589985
"""

import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Derived classes need to override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        rectangle_area = self.length * self.width
        return rectangle_area

class Circle(Shape):
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = Circle.pi * (self.radius ** 2)
        return circle_area