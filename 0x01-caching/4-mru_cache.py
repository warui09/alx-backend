#!/usr/bin/env python3
"""task 4 solution"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """implements MRUCache class"""

    def __init__(self):
        """initialize MRUCache class"""

        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """add item by key to cache"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.mru_key in self.cache_data:
                del self.cache_data[self.mru_key]
                print(f"DISCARD: {self.mru_key}")

        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """get item by key from cache"""

        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        self.mru_key = key

        return value
