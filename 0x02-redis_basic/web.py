#!/usr/bin/env python3
"""
web cache and tracker
"""
from typing import Callable
import requests
import redis
from functools import wraps

_redis = redis.Redis()


def count_reqsts(method: Callable) -> Callable:
    """
    Counts the number of times
    a URL was accessed
    """

    @wraps(method)
    def wrapper(url):
        """
        cache the result with
        an expiration time of 10 seconds.
        """
        _redis.incr("count:{}".format(url), 1)
        txt = "results:{}".format(url)
        r = _redis.get(txt)
        if r:
            return r.decode("utf-8")
        r = method(url)
        _redis.setex(txt, 10, r)
        return r

    return wrapper


@count_reqsts
def get_page(url: str) -> str:
    """Returns HTML content of a url"""
    return requests.get(url).text
