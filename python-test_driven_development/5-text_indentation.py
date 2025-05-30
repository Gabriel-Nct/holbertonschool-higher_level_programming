#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?' and ':'.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".:?":
            result += "\n\n"
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result.strip(), end="")
