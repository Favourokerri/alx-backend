#!/usr/bin/python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class basicCache
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """ method to insert into cache """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ retrives item from cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
