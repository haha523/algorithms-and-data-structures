import os
import unittest
from collections import deque

def process_queue(commands):
    queue = deque()
    output = []

    for command in commands:
        action = command[0]
        if action == '+':
            patient_id = command[1]
            queue.append(patient_id)
        elif action == '*':
            patient_id = command[1]
            mid_index = len(queue) // 2
            if len(queue) % 2 == 0:
                mid_index -= 1
            queue.insert(mid_index + 1, patient_id)
        elif action == '-':
            output.append(queue.popleft())

    return output

class TestClinicQueue(unittest.TestCase):

    def test_example_1(self):
        # given
        commands = [
            ('+', 1),
            ('+', 2),
            ('-', None),
            ('+', 3),
            ('-', None),
            ('-', None)
        ]

        # when
        expected_output = [1, 2, 3]

        # then
        self.assertEqual(process_queue(commands), expected_output)

    def test_example_2(self):
        # given
        commands = [
            ('+', 1),
            ('+', 2),
            ('*', 3),
            ('-', None),
            ('+', 4),
            ('*', 5),
            ('-', None),
            ('-', None),
            ('-', None),
            ('-', None)
        ]

        # when
        expected_output = [1, 3, 2, 5, 4]

        # then
        self.assertEqual(process_queue(commands), expected_output)

if __name__ == '__main__':
    unittest.main()