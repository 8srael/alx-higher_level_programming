#!/usr/bin/python3

def max_integer(my_list=[]):
    maximum = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]

    return maximum
