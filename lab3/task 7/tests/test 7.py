import unittest

def digital_sorting(n, m, k, data):
    strings = [''] * n
    for j in range(m):
        for i in range(n):
            strings[i] += data[j][i]

    indices = list(range(1, n + 1))

    for phase in range(1, k + 1):
        indices.sort(key=lambda x: strings[x - 1][m - phase])

    return indices

class TestDigitalSorting(unittest.TestCase):

    def test_example_1(self):
        # given
        n, m, k = 3, 3, 1
        data = ["bab", "bba", "baa"]
        # when
        result = digital_sorting(n, m, k, data)
        # then
        self.assertEqual(result, [2, 3, 1])

    def test_example_2(self):
        # given
        n, m, k = 3, 3, 2
        data = ["bab", "bba", "baa"]
        # when
        result = digital_sorting(n, m, k, data)
        # then
        self.assertEqual(result, [3, 2, 1])

    def test_example_3(self):
        # given
        n, m, k = 3, 3, 3
        data = ["bab", "bba", "baa"]
        # when
        result = digital_sorting(n, m, k, data)
        # then
        self.assertEqual(result, [2, 3, 1])

    def test_identical_strings(self):
        # given
        n, m, k = 4, 4, 2
        data = ["aaaa", "aaaa", "aaaa", "aaaa"]
        # when
        result = digital_sorting(n, m, k, data)
        # then
        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()