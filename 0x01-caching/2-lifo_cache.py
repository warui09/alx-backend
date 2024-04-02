#!/usr/bin/env python3
"""task 2 solution"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class has two methods
    get: return a cache item by key
    put: assign item to cache by key
    """

    def __init__(self):
        """initialize lifo class"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assign item to cache by key"""

        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.keys.append(key)

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.keys[-2]]
            print(f"DISCARD: {self.keys[-2]}")

    def get(self, key):
        """return item by key"""

        return self.cache_data.get(key, None)
