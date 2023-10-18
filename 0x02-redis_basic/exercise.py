#!/usr/bin/env  python3
""" Contains the class definition for redis cache  """
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


class Cache:
    """
    Defines methods to handle redis cache operations
    """
    def __init__(self, _redis):
        """  Initialize redis client Attributes: """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis cache """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
