#!/usr/bin/env python3
'''
Redis Module
- an open-source in-memory data-structure, NoSQL data store
- can be used as a database and/or cache and message broker
'''

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    Decorator to count method calls and store in Redis.

    Count how many times methods of the Cache class are called.
    Above Cache define a count_calls decorator that takes a single
    method Callable argument and returns a Callable.
    '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key_m= method.__qualname__
        self._redis.incr(key_m)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        '''
        Initializes the Cache class.

        In the __init__ method, store an instance of the Redis client
        as a private variable named _redis (using redis.Redis()) and
        flush the instance using flushdb.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()


    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store the data in Redis using a random key and return the key.

        Create a store method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid), store the
        input data in Redis using the random key and return the key.
        Type-annotate store correctly. Remember that data can be a str, bytes,
        int or float.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        '''
        Redis only allows to store string, bytes and numbers (and lists thereof).
        Retrieve the data stored in Redis using the given key and apply
        the provided transformation function (fn) if available.

        :param key: The key string used to store the data in Redis.
        :param fn: An optional callable to transform the data back to the desired format.
        '''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''
        Retrieve data as a UTF-8 decoded string.
        :param key: The key string used to store the data in Redis.
        '''
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve data as an integer.
        :param key: The key string used to store the data in Redis.
        '''
        return self.get(key, lambda d: int(d))