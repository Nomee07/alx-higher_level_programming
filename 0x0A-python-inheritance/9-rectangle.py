#!/usr/bin/python3


"""Write a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
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

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return self.__str__()
