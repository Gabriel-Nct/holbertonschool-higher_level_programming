#!/usr/bin/python3
"""
Geometry module: Definition of the base geometry class.
This module is class BaseGeometry that defines a Base Geometry.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """

    def __init__(self, size):
        """Initialize a square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square by calling
        the area method of the Rectangle superclass.
        """
        return super().area()

    def __str__(self):
        """
        String representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
