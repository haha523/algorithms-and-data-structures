import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from c3 import process_packets

class TestPacketProcessor(unittest.TestCase):

    def test_process_packets(self):
        # given
        buffer_size = 1
        packets = [(0, 1)]
        expected = [0]
        result = process_packets(buffer_size, packets)
        self.assertEqual(result, expected)

        # when
        buffer_size = 1
        packets = [(0, 1), (0, 1)]
        expected = [0, -1]
        result = process_packets(buffer_size, packets)
        self.assertEqual(result, expected)

        # when
        buffer_size = 1
        packets = [(0, 1), (1, 1)]
        expected = [0, 1]
        result = process_packets(buffer_size, packets)
        self.assertEqual(result, expected)

        # when
        buffer_size = 2
        packets = [(0, 1), (0, 1)]
        expected = [0, 1]
        result = process_packets(buffer_size, packets)
        self.assertEqual(result, expected)

        # when
        buffer_size = 3
        packets = [(0, 1), (1, 1), (2, 1)]
        expected = [0, 1, 2]
        result = process_packets(buffer_size, packets)
        self.assertEqual(result, expected)

        # then
        buffer_size = 2
        packets = [(0, 1), (0, 1), (0, 1)]
        expected = [0, 1, -1]
        result = process_packets(buffer_size, packets)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()