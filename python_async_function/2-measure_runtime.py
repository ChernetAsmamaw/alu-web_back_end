#!/usr/bin/env python3
"""Import wait_n from the previous python file.
Write a function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
"""
import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures time of async funcs.
    Returns float: result
    """
    counter = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    result = perf_counter() - counter
    return result
