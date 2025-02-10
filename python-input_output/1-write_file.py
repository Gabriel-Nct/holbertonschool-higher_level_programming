#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8)

    Args:
        filename (str, optional): The name of the file to write to.
        Defaults to "".
        text (str, optional): The string to write to the file.
        Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
