#!/usr/bin/python3


"""Defines a class that inherits from the list."""


class MyList(list):
    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
