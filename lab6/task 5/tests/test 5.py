import os
import sys
import unittest
from collections import defaultdict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d5 import read_input, write_output

class TestElection(unittest.TestCase):

    def test_read_input(self):
        # given
        test_input = "McCain 10\nObama 5\nMcCain 1\n"
        with open('test_input.txt', 'w') as f:
            f.write(test_input)

        # when
        result = read_input('test_input.txt')
        expected = ['McCain 10\n', 'Obama 5\n', 'McCain 1\n']
        self.assertEqual(result, expected)

        # then
        os.remove('test_input.txt')

    def test_write_output(self):
        # given
        results = [('McCain', 16), ('Obama', 17)]
        write_output('test_output.txt', results)

        # when
        with open('test_output.txt', 'r') as f:
            content = f.readlines()

        # when
        expected_output = ["McCain 16\n", "Obama 17\n"]
        self.assertEqual(content, expected_output)

        # then
        os.remove('test_output.txt')

    def test_vote_count(self):
        # given
        votes = [
            "McCain 10\n",
            "Obama 5\n",
            "McCain 1\n"
        ]
        vote_count = defaultdict(int)

        # when
        for vote in votes:
            parts = vote.split()
            candidate = parts[0]
            count = int(parts[1])
            vote_count[candidate] += count

        # then
        expected_count = {'McCain': 11, 'Obama': 5}
        self.assertEqual(dict(vote_count), expected_count)

if __name__ == "__main__":
    unittest.main()
