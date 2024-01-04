#!/usr/bin/env python3
"""
    Write a function named index_range that takes two integer
    arguments page and page_size.
"""


def index_range(page, page_size):
    """
        returns a tuple of size two
        containing start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    data = (start_index, end_index)
    return data
