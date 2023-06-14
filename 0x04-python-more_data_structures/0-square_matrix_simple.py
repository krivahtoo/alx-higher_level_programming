#!/usr/bin/python3

# computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        result.append([x ** 2 for x in row])
    return result


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
