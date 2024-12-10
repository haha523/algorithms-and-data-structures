import unittest
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)

    mid = len(points) // 2
    mid_point = points[mid]

    dl = closest_pair(points[:mid])
    dr = closest_pair(points[mid:])

    d = min(dl, dr)

    strip = []
    for point in points:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    return min(d, strip_closest(strip, d))

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda point: point[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(strip[i], strip[j]))
            j += 1
    return min_dist

class TestClosestPair(unittest.TestCase):

    def test_two_points(self):
        # given
        points = [(0, 0), (3, 4)]
        # when
        result = closest_pair(points)
        # then
        self.assertAlmostEqual(result, 5.0, places=4)

    def test_identical_points(self):
        # given
        points = [(7, 7), (7, 7)]
        # when
        result = closest_pair(points)
        # then
        self.assertAlmostEqual(result, 0.0, places=4)

    def test_large_set(self):
        # given
        points = [(i, i) for i in range(1000)]
        # when
        result = closest_pair(points)
        # then
        self.assertAlmostEqual(result, math.sqrt(2), places=4)

    def test_scattered_points(self):
        # given
        points = [(1, 1), (2, 2), (3, 3), (10, 10), (12, 12)]
        # when
        result = closest_pair(points)
        # then
        self.assertAlmostEqual(result, math.sqrt(2), places=4)

if __name__ == '__main__':
    unittest.main()