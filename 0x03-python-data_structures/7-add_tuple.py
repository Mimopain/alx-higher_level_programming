#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Use the first two elements of each tuple (or 0 if not present)
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a tuple with the sum of corresponding elements
    return (a[0] + b[0], a[1] + b[1])
