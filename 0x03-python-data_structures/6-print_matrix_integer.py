#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i in range(0, len(x)):
            if i == len(x) - 1:
                print("{:d}".format(x[i]), end='')
            else:
                print("{:d}".format(x[i]), end=' ')
        print('')
