#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats
        div: number to divide by

    Returns:
        New matrix with all elements divided by div, rounded to 2 decimals
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float))
                    for row in matrix for n in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
