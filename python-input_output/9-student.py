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

    def to_json(self):
        """
        Retrieves a dictionary representation of the student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
