#!/usr/bin/python3
"""
LIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFO
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
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_inserted = self.cache_data.popitem()
                print(f"DISCARD: {last_inserted}")
                self.cache_data[key] = item
            self.cache_data[key] = item

    def get(self, key):
        """ retrives item from cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
