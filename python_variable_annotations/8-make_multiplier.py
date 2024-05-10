#!/usr/bin/env python3
"""Annoctated function make_multiplier that takes
a float multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier and returns a function
    and returns Callable[[float], float]: [description]
    """
    return lambda x: x * multiplier
