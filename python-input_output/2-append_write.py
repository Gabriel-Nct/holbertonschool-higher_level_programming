#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)

    Args:
        filename (str, optional): The name of the file to write to.
        Defaults to "".
        text (str, optional): The string to write to the file.
        Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
