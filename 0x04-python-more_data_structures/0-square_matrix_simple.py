#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix or matrix[0] == []:
        return
    new = []

    for row in matrix:
        new.append(list(map(lambda x: x**2, row)))
    return new
