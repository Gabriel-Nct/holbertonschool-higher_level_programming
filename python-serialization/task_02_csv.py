#!/usr/bin/python3
"""
eading data from one format (CSV) and converting
it into another format (JSON) using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    reading data from one format (CSV) and
    converting it into another format (JSON)
    using serialization techniques.

    Args:
        csv_filename: file to convert
    Returns:
        True if the conversion was successful.
        Handle exceptions, such as file not found.
        Function should return False in this case
    """
    try:
        with open(csv_filename, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            csv_content = list(csv_reader)

        with open('data.json', 'w') as file:
            json.dump(csv_content, file)

        return True
    except Exception:
        return False