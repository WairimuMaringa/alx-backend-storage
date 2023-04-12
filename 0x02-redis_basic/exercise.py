#!/usr/bin/env python3
"""
Redis storage basics
"""
import redis
from uuid uuid4
from typing import Union, Callable, Optional
from functools import wraps
UnionOfTypes = Union[str, bytes, int, float]


def
