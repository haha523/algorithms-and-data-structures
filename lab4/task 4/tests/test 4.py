import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b4 import check_brackets

class TestCheckBrackets(unittest.TestCase):

    def test_success_cases(self):
        # given
        self.assertEqual(check_brackets("[]"), "Success")
        self.assertEqual(check_brackets("{}[]"), "Success")
        self.assertEqual(check_brackets("[()]"), "Success")
        self.assertEqual(check_brackets("(())"), "Success")

    def test_first_unmatched_closing(self):
        # given
        self.assertEqual(check_brackets("{[}"), 3)
        self.assertEqual(check_brackets("foo(bar[i);"), 10)

    def test_first_unmatched_opening(self):
        # given
        self.assertEqual(check_brackets("("), 1)
        self.assertEqual(check_brackets("["), 1)
        self.assertEqual(check_brackets("foo(bar)"), "Success")

if __name__ == '__main__':
    unittest.main()