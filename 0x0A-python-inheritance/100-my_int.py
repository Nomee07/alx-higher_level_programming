#!/usr/bin/python3


"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """Override the equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)"""
        return super().__eq__(other)
