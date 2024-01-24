#!/usr/bin/env python3
"""Defining a Class Cache"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        # Getting the current counter value from Redis
        counter = self._redis.get(key)
        if counter:
            counter = int(counter) + 1
        else:
            counter = 1
        # Setting the updated counter value in Redis
        self._redis.set(key, counter)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        inputs_list_key = key + ":inputs"
        output_list_key = key + ":outputs"
        self._redis.rpush(inputs_list_key, str(args))
        key_arg = method(self, *args, **kwds)
        self._redis.rpush(output_list_key, key_arg)
        return key_arg
    return wrapper


class Cache:
    """Class Cache"""
    def __init__(self) -> None:
        """Initializing a new Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument, sets it to a random key and
        returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Reads from Redis and recovers original type"""
        value = self._redis.get(key)
        if not value:
            return None
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> Optional[str]:
        """parametrize get method with string fn"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """parametrize get method with integer fn"""
        return self.get(key, fn=int)
