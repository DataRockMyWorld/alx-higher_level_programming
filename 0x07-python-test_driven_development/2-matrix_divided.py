#!/usr/bin/python3

"""

This module divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """

    All elements of this matrix is divided by div

    Arguments:

    matrix - list of lists

    div - float / integer that does the division

    Retturns a new matrix

    """

    if not matrix:
        raise TypeError("Matrix must be a matrix(list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    x = len(matrix[0])
    new_matrix = []

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError("Matrix must be a matrix(list of lists) of integers/floats")
        if len(row) != x:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (float, int)):
                raise TypeError(
                    "Matrix must be a matrix(list of lists) of integers/floats"
                )
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix
