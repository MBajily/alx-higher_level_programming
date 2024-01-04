#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide elements of matrix.

    Args:
        matrix (list): A list of lists.
        div (int/float): The divisor.
    Raises:
        TypeError: If non-numbers.
        TypeError: If contains rows of different sizes.
        TypeError: If not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        The result of the division.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
    return new_matrix
