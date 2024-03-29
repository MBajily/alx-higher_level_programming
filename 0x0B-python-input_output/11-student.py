#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary the Student.

        Args:
            attrs (list): (Optional) The attributes
        """
        if ((type(attrs) == list) and all(type(e) == str for e in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes

        Args:
            json (dict): The key/value pairs
        """
        for key, value in json.items():
            setattr(self, key, value)
