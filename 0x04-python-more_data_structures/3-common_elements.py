#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set_1 = set(set_1)
    new_set_2 = set(set_2)
    common_result = new_set_1 & new_set_2
    return common_result
