#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        i = 0
        for element in row:
            if i == 2:
                print("{:d}".format(element))
            else:
                print("{:d}".format(element), end=" ")
            i += 1
