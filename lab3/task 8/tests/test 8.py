import unittest
from typing import List, Tuple
import heapq

def k_closest_points(points: List[Tuple[int, int]], K: int) -> List[Tuple[int, int]]:
    return heapq.nsmallest(K, points, key=lambda p: p[0]**2 + p[1]**2)

class TestKClosestPoints(unittest.TestCase):

    def test_example_1(self):
        points = [(2, 1), (1, 3), (-2, 2)]
        K = 1
        result = k_closest_points(points, K)
        self.assertEqual(result, [(2, 1)])

    def test_example_2(self):
        points = [(3, 2), (3, 3), (5, -1), (-2, 4)]
        K = 2
        result = k_closest_points(points, K)
        expected = [(3, 2), (3, 3)]
        self.assertTrue(all(item in expected for item in result))
        self.assertEqual(len(result), K)

    def test_multiple_closest(self):
        points = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        K = 2
        result = k_closest_points(points, K)
        expected = [(1, 1), (1, -1)]
        self.assertTrue(all(item in expected for item in result))
        self.assertEqual(len(result), K)

    def test_k_greater_than_points(self):
        points = [(1, 2), (3, 4)]
        K = 5
        result = k_closest_points(points, K)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()