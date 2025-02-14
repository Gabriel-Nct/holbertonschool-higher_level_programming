#!/usr/bin/python3
"""
Serialize and Deserialize custom Python objects using the pickle module.
"""
import pickle


class CustomObject:
    """
    a custom Python class named CustomObject
    """
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initializes name, age and is_student.

        Args:
            name (str): a string
            age (int): an integer
            is_student (bool): a boolean
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Method to print out the object’s attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Using the pickle module,
        it will serialize the current instance of the object
        and save it to the provided filename.
        Args:
            filename (str): a string
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        """
        Using the pickle module,
        it will load and return an instance of the CustomObject
        from the provided filename.
        Args:
            filename (str): a string

        Returns:
            an instance of the CustomObject from the provided filename
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
