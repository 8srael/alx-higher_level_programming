#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map((lambda z: z * z), number)) for number in matrix]
