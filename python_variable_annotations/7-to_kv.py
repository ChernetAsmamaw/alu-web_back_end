#!/usr/bin/env python3
"""Annoctated  function sum_mixed_list which
takes a list mxd_lst of integers and floats
and returns their sum as a float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int OR
    float v as arguments and returns a tuple.
    Tuple[str, float]: [description]
    """
    return (k, v**2)
