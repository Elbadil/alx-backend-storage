#!/usr/bin/env python3
"""Defining a Class Cache"""
import redis
import uuid
from typing import Union


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
