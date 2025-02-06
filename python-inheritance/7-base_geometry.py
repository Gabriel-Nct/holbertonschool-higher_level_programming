#!/usr/bin/python3
"""
Geometry module: Definition of the base geometry class.
This module is class BaseGeometry that defines a Base Geometry.
"""


class BaseGeometry:
    """
    A class called BaseGeometry.
    """
    def area(self):
        """Raises an exception indicating that the area method is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
