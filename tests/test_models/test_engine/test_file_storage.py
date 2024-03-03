#!/usr/bin/python3
import unittest
import os
from models import FileStorage
from models.base_model import BaseModel

"""
Unittest FileStorage
"""


class FileStorage_Test(unittest.TestCase):

    def test_all(self):
        """tests all method"""
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
