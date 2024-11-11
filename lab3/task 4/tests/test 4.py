import unittest

def count_segments_containing_points(segments, points):
    events = []

    for a, b in segments:
        events.append((a, 'start'))  # Bắt đầu đoạn
        events.append((b, 'end'))    # Kết thúc đoạn (b là bao gồm)

    for i, x in enumerate(points):
        events.append((x, 'point', i))  # Ghi chỉ số điểm

    events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else (1 if x[1] == 'point' else 2)))

    count = 0
    results = [0] * len(points)

    for event in events:
        if event[1] == 'start':
            count += 1
        elif event[1] == 'end':
            count -= 1
        elif event[1] == 'point':
            index = event[2]
            results[index] = count

    return results

class TestCountSegments(unittest.TestCase):

    def test_case_1(self):
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected = [1, 0, 0]
        result = count_segments_containing_points(segments, points)
        self.assertEqual(result, expected)

    def test_case_2(self):
        segments = [(-10, 10)]
        points = [-100, 100, 0]
        expected = [0, 0, 1]
        result = count_segments_containing_points(segments, points)
        self.assertEqual(result, expected)

    def test_case_3(self):
        segments = [(0, 5), (-3, 2), (7, 10)]
        points = [1, 6]
        expected = [2, 0]
        result = count_segments_containing_points(segments, points)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()