#!/usr/bin/python3
"""task 0 solution"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache  defines two methods
    -put: for adding data to the cache
    -get: retrieve data from the cache
    """

    def put(self, key, item):
        """Add an item to the cache"""

        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""

        return self.cache_data.get(key, None)
