#!/usr/bin/env python3
'''
Redis Module
- an open-source in-memory data-structure, NoSQL data store
- can be used as a database and/or cache and message broker
'''

import redis
import uuid
from typing import Union


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