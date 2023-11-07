#!/usr/bin/python3


"""Reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str, optional): The name of the file to be read.

    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
