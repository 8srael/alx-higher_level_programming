#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_del_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            list_del_jeys.append(key)

    for key in list_del_keys:
        del a_dictionary[key]

    return a_dictionary
