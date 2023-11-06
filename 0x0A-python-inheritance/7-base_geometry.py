#!/usr/bin/python3


"""Writes a class BaseGeometry."""


class BaseGeometry:
    def area(self):
        """Raises an Exception with the message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
