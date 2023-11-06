#!/usr/bin/python3


"""Write a class MyInt that inherits from int"""


class MyInt(int):
    def __eq__(self, other):
        """Override the equality operator (==).

        Inverts the behavior of the equality operator.

        Args:
            other: The other value to compare for equality.

        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)"""
        return super().__eq__(other)
