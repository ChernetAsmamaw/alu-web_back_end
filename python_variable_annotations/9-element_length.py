#!/usr/bin/env python3
"""Annoctate a function's parameters and return values
with appropriate types
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list
        List[Tuple[Sequence, int]]: a tuple
    """
    return [(x, len(x)) for x in lst]
