#!/usr/bin/python3


"""Writes a string to s text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file

    Args:
        filename (str, optional): The name of the file.
        text (str): The string to be written to the file.

    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
