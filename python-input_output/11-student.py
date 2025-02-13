#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student with the provided
        first name, last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student instance.

        Args:
        attrs (list, optional): A list of attribute names
        to include in the dictionary.
        If None, all attributes are included. Default is None.

        Returns:
        dict: A dictionary containing the student's specified attributes.
        If attrs is provided, only the specified attributes are included.
        """
        if attrs is None:
            return self.__dict__
        elif (
            isinstance(attrs, list)
            and all(isinstance(element, str) for element in attrs)
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """
        Replaces the attributes of the Student instance
        with values from a dictionary.

        Args:
        json (dict): A dictionary where keys are
        attribute names and values are the new values.

        The method updates only the attributes
        that already exist in the instance.

        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
