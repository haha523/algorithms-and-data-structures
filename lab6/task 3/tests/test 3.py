import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d3 import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        # given
        self.hash_table = HashTable(5)

    def test_add_and_find(self):
        # given
        self.hash_table.add("test")
        # when
        self.assertEqual(self.hash_table.find("test"), "yes")
        # then
        self.assertEqual(self.hash_table.find("not_in_table"), "no")

    def test_delete(self):
        # given
        self.hash_table.add("test")
        # when
        self.hash_table.delete("test")
        # then
        self.assertEqual(self.hash_table.find("test"), "no")

    def test_check(self):
        # given
        self.hash_table.add("hello")
        # when
        self.hash_table.add("world")
        # then
        self.assertEqual(self.hash_table.check(0), "hello")

    def test_case_sensitivity(self):
        # given
        self.hash_table.add("Test")
        # when
        self.assertEqual(self.hash_table.find("test"), "no")
        # then
        self.assertEqual(self.hash_table.find("Test"), "yes")

if __name__ == "__main__":
    unittest.main()
