#!/usr/bin/env python3
"""Argumenting a function in the correct duck-typed
annotations that takes a sequence and returns its
first element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Take a sequence lst and return its first element:
        Union[Any, None]: None or first element
    """
    if lst:
        return lst[0]
    else:
        return None
