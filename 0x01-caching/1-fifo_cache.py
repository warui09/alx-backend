#!/usr/bin/env python3
"""task 1 solution"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class has two methods:
    get: returns items in the cache by key
    put: assign items to the cache
    """

    def __init__(self):
        """initialize fifo class"""

        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assign item to the cache"""

        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.keys.append(key)

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.keys[0]]
            print(f"DISCARD: {self.keys[0]}")

    def get(self, key):
        """return item by key"""

        return self.cache_data.get(key, None)
