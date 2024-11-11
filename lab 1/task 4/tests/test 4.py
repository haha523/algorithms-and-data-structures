import unittest


def linear_search(arr, v):
    indices = [i for i, x in enumerate(arr) if x == v]

    if len(indices) > 0:
        return f"{len(indices)}: " + ', '.join(map(str, indices))
    else:
        return "-1"


class TestLinearSearch(unittest.TestCase):

    def test_value_present_once(self):
        arr = [1, 2, 3, 4, 5]
        v = 3
        result = linear_search(arr, v)
        self.assertEqual(result, "1: 2")

    def test_value_present_multiple_times(self):
        arr = [1, 2, 3, 2, 5]
        v = 2
        result = linear_search(arr, v)
        self.assertEqual(result, "2: 1, 3")

    def test_value_not_present(self):
        arr = [1, 2, 3, 4, 5]
        v = 6
        result = linear_search(arr, v)
        self.assertEqual(result, "-1")

    def test_empty_array(self):
        arr = []
        v = 1
        result = linear_search(arr, v)
        self.assertEqual(result, "-1")

    def test_value_at_start(self):
        arr = [10, 20, 30, 40]
        v = 10
        result = linear_search(arr, v)
        self.assertEqual(result, "1: 0")

    def test_value_at_end(self):
        arr = [10, 20, 30, 40]
        v = 40
        result = linear_search(arr, v)
        self.assertEqual(result, "1: 3")

    def test_value_with_duplicates(self):
        arr = [5, 5, 5, 5]
        v = 5
        result = linear_search(arr, v)
        self.assertEqual(result, "4: 0, 1, 2, 3")


if __name__ == '__main__':
    unittest.main()
