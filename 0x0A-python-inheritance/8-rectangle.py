#!/usr/bin/python3
"""Defines a class Rectangle(BaseGeometry)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents rectangle by BaseGeometry."""

    def __init__(self, width, height):
        """Intialization

        Args:
            width (int): width of Rectangle.
            height (int): height of Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
