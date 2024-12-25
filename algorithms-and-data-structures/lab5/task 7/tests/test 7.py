import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c7 import heap_sort, read_input, write_output

class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        # given
        input_data = "5\n5 2 9 1 5\n"
        expected_output = "1 2 5 5 9\n"

        # when
        with open(os.path.join('..', 'txtf', 'input.txt'), 'w') as f:
            f.write(input_data)

        # when
        arr = read_input(os.path.join('..', 'txtf', 'input.txt'))

        # when
        heap_sort(arr)

        # when
        write_output(os.path.join('..', 'txtf', 'output.txt'), arr)

        # when
        with open(os.path.join('..', 'txtf', 'output.txt'), 'r') as f:
            result = f.read().strip()

        # then
        self.assertEqual(result, expected_output.strip())

if __name__ == "__main__":
    unittest.main()