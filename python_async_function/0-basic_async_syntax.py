#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer
argument that waits for a random delay between 0 and
max_delay seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns float: random float number"""
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
