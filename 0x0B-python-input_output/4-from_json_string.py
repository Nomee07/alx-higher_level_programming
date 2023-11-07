#!/usr/bin/python3


import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python
    """
    return json.loads(my_str)
