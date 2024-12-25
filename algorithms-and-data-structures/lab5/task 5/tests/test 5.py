import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c5 import task_scheduler

class TestTaskScheduler(unittest.TestCase):
    def test_example_1(self):
        # given
        input_data = "2 5\n1 2 3 4 5\n"
        expected_output = "0 0\n1 0\n0 1\n1 2\n0 4\n"

        # when
        with open(os.path.join('..', 'txtf', 'input.txt'), 'w') as f:
            f.write(input_data)

        # when
        task_scheduler()

        # when
        with open(os.path.join('..', 'txtf', 'output.txt'), 'r') as f:
            result = f.read()

        # then
        self.assertEqual(result, expected_output)

    def test_example_2(self):
        # given
        input_data = "4 20\n" + "1 " * 20 + "\n"
        expected_output = "\n".join([
            f"{i % 4} {i // 4}"
            for i in range(20)
        ]) + "\n"

        # when
        with open(os.path.join('..', 'txtf', 'input.txt'), 'w') as f:
            f.write(input_data)

        # when
        task_scheduler()

        # when
        with open(os.path.join('..', 'txtf', 'output.txt'), 'r') as f:
            result = f.read()

        # then
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()