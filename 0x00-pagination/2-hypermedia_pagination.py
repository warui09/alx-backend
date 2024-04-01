#!/usr/bin/env python3
"""task 1 solution"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """paginate dataset"""

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        def index_range(page: int, page_size: int) -> tuple:
            """return stating and ending indices"""

            start_index = (page - 1) * page_size
            end_index = page * page_size
            return (start_index, end_index)

        start_index, end_index = index_range(page, page_size)

        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dict with relevant info"""

        info = self.get_page(page, page_size)
        data = self.get_page(page, page_size)
        total_pages = math.ceil((len(self.dataset()) + 1) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
