#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    # Initialize the result with 0
    result = 0
    # iterating through the remaining number
    for num in new_list:
        result += num
    return result
