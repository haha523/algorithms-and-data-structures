import unittest

def generate_anti_quick_sort(n):
    result = []
    for i in range(1, n + 1, 2):
        result.append(i)
    for i in range(2, n + 1, 2):
        result.append(i)
    return result

class TestAntiQuickSort(unittest.TestCase):

    def test_n_equals_1(self):
        # given
        self.assertEqual(generate_anti_quick_sort(1), [1])

    def test_n_equals_2(self):
        # given
        self.assertEqual(generate_anti_quick_sort(2), [1, 2])

    def test_n_equals_3(self):
        # given
        self.assertEqual(generate_anti_quick_sort(3), [1, 3, 2])

    def test_n_equals_4(self):
        # given
        self.assertEqual(generate_anti_quick_sort(4), [1, 3, 2, 4])

if __name__ == '__main__':
    unittest.main()