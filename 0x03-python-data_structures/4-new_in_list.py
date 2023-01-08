#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(0, len(my_list)):
            new_list.append(my_list[i])
        new_list[idx] = element
        return new_list
