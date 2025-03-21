#!/usr/bin/python3
"""Module 5-Rectangle: Definition of the Rectangle class.

This module is class Rectangle that defines a rectangle
by: (based on 4-rectangle.py)

"""


class Rectangle:
    """Rectangle with width

    """
    def __init__(self, width=0, height=0):
        """
        give the width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        give the width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """"
        set the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """"
        give the height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        set the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return the area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        return the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_to_print = ""
            for index in range(self.__height):
                rectangle_to_print += "#" * self.__width
                if index != self.__height - 1:
                    rectangle_to_print += "\n"
            return rectangle_to_print

    def __repr__(self):
        """
        return a string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print message when an instance is deleted
        """
        print("Bye rectangle...")
