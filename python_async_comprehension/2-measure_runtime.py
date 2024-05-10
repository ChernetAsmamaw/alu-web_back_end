#!/usr/bin/env python3
"""Import async_comprehension and write a measure_runtime
coroutine that'll execute async_comprehension 4x in parallel using
asyncio.gather. measure_runtime should measure total runtime & return it.
"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns: float: measure"""
    start = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time()
    return end - start
