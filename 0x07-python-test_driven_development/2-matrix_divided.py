#!/usr/bin/python3
"""
1. Divide a matrix
Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix. """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or type(matrix[0]) != list:
        raise TypeError(type_err)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div = float(div)
    row_len = len(matrix[0])
    new_matrix = [[0.0 for _ in range(row_len)] for _ in range(len(matrix))]
    for i, y in enumerate(matrix):
        if len(y) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for j, x in enumerate(y):
            if type(x) != int and type(x) != float:
                raise TypeError(type_err)
            new_matrix[i][j] = round(x / div, 2)
    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
