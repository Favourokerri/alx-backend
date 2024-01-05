#!/usr/bin/python3
"""
lru_cache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ class LRUCache
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
                key (_type_): _description_
                item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = next(iter(self.cache_data.keys()))
                del self.cache_data[discard_key[0]]
                print(f"DISCARD: {discard_key[0]}")
                self.cache_data[key] = item
            self.cache_data[key] = item

    def get(self, key):
        """ retrives item from cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
