#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i in range(0, len(x)):
            if i == len(x) - 1:
                print("{}".format(x[i]), end='')
            else:
                print("{}".format(x[i]), end=' ')
        print('')
