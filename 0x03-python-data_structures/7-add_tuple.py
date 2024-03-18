#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < len(tuple_a):
        tuple_b += (0,) * (len(tuple_a) - len(tuple_b))
    elif len(tuple_a) < len(tuple_b):
        tuple_a += (0,) * (len(tuple_b) - len(tuple_a))
    # If a tuple is bigger than 2, use only the first 2 integers
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple
