#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98       # LOAD_CONST 1 (98)
    result += a       # LOAD_FAST 0 (a)
    result = result ** b  # LOAD_FAST 1 (b), BINARY_POWER
    return result     # BINARY_ADD, RETURN_VALUE

