from contextlib import AbstractContextManager
from typing import Any
import unittest
import sys
sys.path.append('..')
from mongo_vector_search_example import vector_search_data

class TestVectorSearchData(unittest.TestCase):
    def test_vector_search_data(self):
        vector_search_data('Who is Goku?')

if __name__ == '__main__':
    unittest.main()