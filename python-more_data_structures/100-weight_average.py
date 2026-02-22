#!/usr/bin/python3
"""Function that returns the weighted average of all integers tuple."""


def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = sum(score * weight for score, weight in my_list)
    weights = sum(weight for score, weight in my_list)
    return total / weights
