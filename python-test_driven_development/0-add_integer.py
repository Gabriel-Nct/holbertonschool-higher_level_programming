#!/usr/bin/python3
"""
This module is conceived to add two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number, default is 98.
    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    Returns:
        int: The sum of `a` and `b`.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
