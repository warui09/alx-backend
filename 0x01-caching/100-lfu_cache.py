#!/usr/bin/env python3
"""task 5 solution"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """define LFUCache class"""

    def __init__(self):
        """initialize LFUCache class"""

        super().__init__()
        self.frequency = {}
        self.least_freq_used = None

    def put(self, key, item):
        """add item to cache by key"""

        if key is None or item is None:
            return

        self.cache_data[key] = item

        # Update frequency
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        # Update least frequently used key
        if (
            self.least_freq_used is None
            or self.frequency[key] < self.frequency[self.least_freq_used]
        ):
            self.least_freq_used = key

        # Discard items if cache is full
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self._discard()

    def get(self, key):
        """get item from cache by key"""

        if key in self.cache_data:
            # Update frequency
            self.frequency[key] += 1

            # Update least frequently used key
            if (
                key == self.least_freq_used
                or self.frequency[key] < self.frequency[self.least_freq_used]
            ):
                self.least_freq_used = key

            return self.cache_data[key]

        return None

    def _discard(self):
        """discard the least frequency used item"""

        if self.least_freq_used in self.cache_data:
            del self.cache_data[self.least_freq_used]
            del self.frequency[self.least_freq_used]
            print(f"DISCARD: {self.least_freq_used}")

            # Find the next least frequently used key
            min_freq = min(self.frequency.values())
            self.least_freq_used = min(
                key for key, value in self.frequency.items()\
                        if value == min_freq
            )
