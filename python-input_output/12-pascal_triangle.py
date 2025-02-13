#!/usr/bin/python3
"""
function that eturns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n line using recursion.

    Args:
        n (int): The number of line in the triangle.

    Returns:
        A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    triangle = pascal_triangle(n - 1)
    last_line = triangle[-1]
    new_line = [1]

    for count in range(1, len(last_line)):
        new_line.append(last_line[count - 1] + last_line[count])

    new_line.append(1)
    triangle.append(new_line)

    return triangle
