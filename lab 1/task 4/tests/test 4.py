import unittest

def linear_search(arr, v):
    indices = [i for i, x in enumerate(arr) if x == v]

    if len(indices) > 0:
        return f"{len(indices)}: " + ', '.join(map(str, indices))
    else:
        return "-1"

class TestLinearSearch(unittest.TestCase):

    def test_value_present_once(self):
        # given
        arr = [1, 2, 3, 4, 5]
        v = 3
        # when
        result = linear_search(arr, v)
        # then
        self.assertEqual(result, "1: 2")

    def test_value_present_multiple_times(self):
        # given
        arr = [1, 2, 3, 2, 5]
        v = 2
        # when
        result = linear_search(arr, v)
        # then
        self.assertEqual(result, "2: 1, 3")

    def test_value_not_present(self):
        # given
        arr = [1, 2, 3, 4, 5]
        v = 6
        # when
        result = linear_search(arr, v)
        # then
        self.assertEqual(result, "-1")

    def test_empty_array(self):
        # given
        arr = []
        v = 1
        # when
        result = linear_search(arr, v)
        # then
        self.assertEqual(result, "-1")

    def test_value_at_start(self):
        # given
        arr = [10, 20, 30, 40]
        v = 10
        # when
        result = linear_search(arr, v)
        # then
        self.assertEqual(result, "1: 0")

    def test_value_at_end(self):
        # given
        arr = [10, 20, 30, 40]
        v = 40
        # when
        result = linear_search(arr, v)
        # then
        self.assertEqual(result, "1: 3")

    def test_value_with_duplicates(self):
        # given
        arr = [5, 5, 5, 5]
        v = 5
        # when
        result = linear_search(arr, v)

        # then
        self.assertEqual(result, "4: 0, 1, 2, 3")

if __name__ == '__main__':
    unittest.main()
