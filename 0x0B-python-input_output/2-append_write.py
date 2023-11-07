#!/usr/bin/python3


"""Appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file

    Args:
        filename (str, optional): The name of the file.
        text (str): The string to be appended to the file.

    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            num_chars_added = file.write(text)
        return num_chars_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
