#!/usr/bin/python3
"""Module 3-square: Definition of the Square class.

This module class Square that defines a square by: (based on 2-square.py)

"""


class Square:
    """Square with size

    """
    def __init__(self, size=0):
        """
        give the size
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """
        give the area of the square
        """
        return (self.__size * self.__size)
