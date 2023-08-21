#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self,
                        index: int = None, page_size: int = 10) -> Dict:
        """
            get_hyper_index method with two integer arguments: index with a
            None default value and page_size with default value of 10
        """
        assert index is None or(isinstance(index, int) and 0 <= index <
                len(self.__indexed_dataset))
        data = []
        next_i = index + page_size if index is not None else None
        
        if index is not None:
            end_i = min(index + page_size, len(self.__indexed_dataset))
            data = [self.__indexed_dataset[i] for i in range(index, end_i) if i in self.__indexed_dataset]

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_i
        }
