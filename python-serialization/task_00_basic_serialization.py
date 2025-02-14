#!/usr/bin/python3
"""
A basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file and
deserialize the JSON file to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    The function serialize and save data to the specified file
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
        If the output file already exists it should be replaced.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_and_deserialize(filename):
    """
    The function load and deserialize data from the specified file
    Args:
        filename: The filename of the input JSON file
        This function returns a Python Dictionary with
        the deseialized JSON data from the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
