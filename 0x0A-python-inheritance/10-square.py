#!/usr/bin/python3


"""Write a class Square that inherits from Rectangle"""


class Square(Rectangle):
    def __init__(self, size):
        """
        Initialize a Square instance with a specified size.

        Args:
            size (int): The size of the square (positive integer).

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """Return a string representation of the square."""
        return self.__str__()
