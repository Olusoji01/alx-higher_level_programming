#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0
    keys = list(a_dictionary)
    for i in range(0, len(keys)):
        count += 1
    return count
