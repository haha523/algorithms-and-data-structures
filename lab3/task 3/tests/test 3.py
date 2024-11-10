import unittest

def can_sort_with_k(n, k, sizes):
    groups = [[] for _ in range(k)]

    for i in range(n):
        groups[i % k].append(sizes[i])

    for group in groups:
        group.sort()

    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])

    return sorted_sizes == sorted(sizes)


class TestSortWithK(unittest.TestCase):

    def test_sortable_cases(self):
        self.assertTrue(can_sort_with_k(5, 3, [1, 5, 3, 4, 1]))  # ДА
        self.assertFalse(can_sort_with_k(3, 2, [2, 1, 3]))  # НЕТ
        self.assertFalse(can_sort_with_k(6, 2, [6, 5, 4, 3, 2, 1]))  # НЕТ
        self.assertTrue(can_sort_with_k(4, 1, [3, 1, 2, 4]))  # ДА
        self.assertFalse(can_sort_with_k(4, 2, [4, 3, 2, 1]))  # НЕТ

    def test_edge_cases(self):
        self.assertTrue(can_sort_with_k(1, 1, [1]))  # ДА
        self.assertTrue(can_sort_with_k(2, 1, [1, 2]))  # ДА
        self.assertTrue(can_sort_with_k(2, 1, [2, 1]))  # ДА
        self.assertTrue(can_sort_with_k(3, 3, [1, 2, 3]))  # ДА
        self.assertFalse(can_sort_with_k(3, 3, [3, 2, 1]))  # НЕТ

if __name__ == '__main__':
    unittest.main()