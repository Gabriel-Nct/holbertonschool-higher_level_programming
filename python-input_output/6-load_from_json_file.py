#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”
    Args:
    filename (no type): the file with we creates an Object
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        convert = json.loads(content)
        return convert
