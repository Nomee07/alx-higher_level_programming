#!/usr/bin/python3

"""Writes a class Rectangle."""


class Rectangle:
    def __init__(self, width, height):
        """Initialize a Rectangle instance with a specified width and height.

        Args:
            width (int): The width of the rectangle (positive integer).
            height (int): The height of the rectangle (positive integer).

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
