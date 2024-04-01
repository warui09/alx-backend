#!/usr/bin/env python3
"""task 0 solution"""


def index_range(page: int, page_size: int) -> tuple:
    """
    returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """

    start_index = (page - 1) * page_size if page > 1 else 0
    end_index = page * page_size

    return (start_index, end_index)
