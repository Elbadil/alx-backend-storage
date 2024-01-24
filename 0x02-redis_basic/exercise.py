#!/usr/bin/env python3
"""Defining a Class Cache"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """Class Cache"""
    def __init__(self) -> None:
        """Initializing a new Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument, sets it to a random key and
        returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]):
        """"""
        value = self._redis.get(key)
        if not value:
            return None
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> Callable:
        """Converts the value to a string"""
        return self.get(self, key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key) -> Callable:
        """Converts the value to integer"""
        return self.get(self, key, fn=int)
