import unittest

def digital_sorting(n, m, k, data):
    strings = [''] * n
    for j in range(m):
        for i in range(n):
            strings[i] += data[j][i]

    indices = list(range(1, n + 1))

    for phase in range(1, k + 1):
        # Sắp xếp theo ký tự ở vị trí m - phase
        indices.sort(key=lambda x: strings[x - 1][m - phase])

    return indices

class TestDigitalSorting(unittest.TestCase):

    def test_example_1(self):
        n, m, k = 3, 3, 1
        data = ["bab", "bba", "baa"]
        result = digital_sorting(n, m, k, data)
        self.assertEqual(result, [2, 3, 1])

    def test_example_2(self):
        n, m, k = 3, 3, 2
        data = ["bab", "bba", "baa"]
        result = digital_sorting(n, m, k, data)
        self.assertEqual(result, [3, 2, 1])

    def test_example_3(self):
        n, m, k = 3, 3, 3
        data = ["bab", "bba", "baa"]
        result = digital_sorting(n, m, k, data)
        self.assertEqual(result, [2, 3, 1])

    def test_identical_strings(self):
        n, m, k = 4, 4, 2
        data = ["aaaa", "aaaa", "aaaa", "aaaa"]
        result = digital_sorting(n, m, k, data)
        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()