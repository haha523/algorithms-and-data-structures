import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from e7 import is_match, read_input, write_output

class TestPatternMatching(unittest.TestCase):

    def test_matching_cases(self):
        # given
        self.assertTrue(is_match("k?t*n", "kitten"))
        self.assertTrue(is_match("a?b", "acb"))
        # when
        self.assertTrue(is_match("k*t*n", "kitten"))
        self.assertTrue(is_match("c*", "cat"))
        # then
        self.assertTrue(is_match("*", "anything"))
        self.assertTrue(is_match("", ""))

    def test_non_matching_cases(self):
        # given
        self.assertFalse(is_match("k?t?n", "kitten"))
        self.assertFalse(is_match("a?b", "ab"))
        # when
        self.assertFalse(is_match("k*t*n", "kittening"))
        self.assertFalse(is_match("c*", "bat"))
        # then
        self.assertFalse(is_match("abc", "abd"))
        self.assertFalse(is_match("", "non-empty"))

if __name__ == '__main__':
    unittest.main()
