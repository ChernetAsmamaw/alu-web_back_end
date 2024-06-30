#!/usr/bin/env python3
'''
Main file
'''
import redis

# Test writing strings to Redis
Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))


# Test reading from Redis and recovering original type
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    retrieved_value = cache.get(key, fn=fn)
    print(f"Stored value: {value}, Retrieved value: {retrieved_value}")
    assert retrieved_value == value


# Test INCR incrimenting values

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))


# Test