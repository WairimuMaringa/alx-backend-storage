#!/usr/bin/env python3
"""
Redis storage basics
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps
UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """ Count no of times cache is called. """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ the wrapper function. """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ History of inputs and outputs. """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ the wrapper function. """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def replay(method: Callable) -> None:
    """ Replays function history. """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """ cache class. """
    def __init__(self):
        """ Reddis db. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self,
              data: UnionOfTypes) -> str:
        """ Store data. """
        randomkey = str(uuid4())
        self._redis.mset({randomkey: data})
        return randomkey

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
