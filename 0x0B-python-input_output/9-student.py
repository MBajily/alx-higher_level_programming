#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary of student."""
        return self.__dict__
