#!/usr/bin/env python3
"""Annoctated function that takes a list of float numbers
and returns the sum of all float numbers in the list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of float numbers and returns
    float: return sum of all float number in a list
    """
    return float(sum(input_list))
