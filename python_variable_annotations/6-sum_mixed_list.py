#!/usr/bin/env python3
"""Annoctated function that takes a list of
integers and floats and returns their sum
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and returns
    float: result
    """
    return float(sum(mxd_lst))
