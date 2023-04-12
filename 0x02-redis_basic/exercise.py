#!/usr/bin/env python3
"""
Redis storage basics
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps
UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """ cache class. """
    def __init__(self):
        """ Reddis db. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """ Store data. """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> UnionOfTypes:
        """ Get data. """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, data: str) -> str:
        """ Get string. """
        return self.get(key, str)

    def get_int(self, data: str) -> int:
        """ Get int. """
        return self.get(key, int)
