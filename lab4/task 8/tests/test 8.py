import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from b8 import evaluate_postfix

class TestPostfixEvaluator(unittest.TestCase):

    def test_basic_operations(self):
        # given
        self.assertEqual(evaluate_postfix(['2', '3', '+']), 5)
        self.assertEqual(evaluate_postfix(['5', '1', '2', '+', '4', '*', '+']), 17)
        self.assertEqual(evaluate_postfix(['4', '2', '-']), 2)
        self.assertEqual(evaluate_postfix(['0', '0', '+']), 0)

    def test_complex_expression(self):
        # given
        self.assertEqual(evaluate_postfix(['3', '4', '+', '2', '*', '7', '-']), 7)
        self.assertEqual(evaluate_postfix(['8', '9', '+', '1', '7', '-', '*']), -102)

    def test_edge_cases(self):
        # given
        self.assertEqual(evaluate_postfix(['1']), 1)

if __name__ == '__main__':
    unittest.main()