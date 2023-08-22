#!/usr/bin/env python3
"""
    Write a function named index_range that takes two integer
    arguments page and page_size.
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
        named index_range takes two integer arguments page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            get_page takes two integer arguments page with default value 1
            and page_size with default value 10
        """
        assert isinstance(page, int) and page > 0
        # "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0
        # "Page size should be a positive integer"
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start: end]
