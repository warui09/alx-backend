#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns dict"""

        assert index < len(self.dataset()) - 1

        data = self.get_page(index, page_size)

        if len(data) < page_size:
            data = self.indexed_dataset().values[index, index + page_size]

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": index + page_size,
        }
