#!/usr/bin/python3
"""Magic calculation based on bytecode"""
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """Reproduce the given bytecode"""
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
