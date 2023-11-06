#!/usr/bin/python3


"""Checks if the object is an instance."""


def inherits_from(obj, a_class):
    """Checks if the given object is an instance of a class.

    Args:
        The object to check.
    """

    return issubclass(type(obj), a_class)
