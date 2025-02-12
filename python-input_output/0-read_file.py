#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function which open and reads a file.txr
    Args:
        filename (str): Text to open. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
