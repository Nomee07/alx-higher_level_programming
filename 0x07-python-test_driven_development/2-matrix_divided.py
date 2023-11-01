#!/usr/bin/python3


"""Defines elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix of integers or floats.
        div (int or float): The number to divide all elements by
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise ValueError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        new_matrix.append(new_row)

    return new_matrix
