#!/usr/bin/python3


"""Adds a new attribute to an object."""


def add_new_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to the object if it's possible.

    Args:
        obj: The object to which the attribute will be added.
        attr_name (str): The name of the new attribute.
        attr_value: The value of the new attribute.

    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute "
                        "if the object can't have new attribute")
