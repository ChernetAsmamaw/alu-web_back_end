#!/usr/bin/env python3
"""Zoom array module. Use mypy to validate the
following piece of code and apply any necessary changes.
"""

from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with range 2 or factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
