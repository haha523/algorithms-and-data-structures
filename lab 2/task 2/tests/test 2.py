import unittest
import os
from io import StringIO
import sys

def merge(arr, left, mid, right, output):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left


    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


    output.write(f"{left + 1} {right + 1} {arr[left]} {arr[right]}\n")


def merge_sort(arr, left, right, output):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, output)
        merge_sort(arr, mid + 1, right, output)
        merge(arr, left, mid, right, output)

# Класс для тестирования алгоритма сортировки
class TestMergeSort(unittest.TestCase):
    def setUp(self):
        # given
        self.output = StringIO()  # Создаем поток для вывода

    # Тест для уже отсортированного массива
    def test_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        merge_sort(arr, 0, len(arr) - 1, self.output)
        # when
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        # then
        self.assertIn("1 5 1 5\n", self.output.getvalue())

    # Тест для массива, отсортированного в обратном порядке
    def test_reverse_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        merge_sort(arr, 0, len(arr) - 1, self.output)
        # when
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        # then
        self.assertIn("1 5 1 5\n", self.output.getvalue())

    # Тест для неотсортированного массива
    def test_unsorted_array(self):
        # given
        arr = [3, 1, 4, 2, 5]
        merge_sort(arr, 0, len(arr) - 1, self.output)
        # when
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        # then
        self.assertIn("1 5 1 5\n", self.output.getvalue())

    # Тест для пустого массива
    def test_empty_array(self):
        # given
        arr = []
        merge_sort(arr, 0, len(arr) - 1, self.output)
        # when
        self.assertEqual(arr, [])
        # then
        self.assertEqual(self.output.getvalue(), "")

    # Тест для массива с одним элементом
    def test_single_element_array(self):
        # given
        arr = [42]
        merge_sort(arr, 0, len(arr) - 1, self.output)
        # when
        self.assertEqual(arr, [42])
        # then
        self.assertEqual(self.output.getvalue(), "")

    # Тест для массива с дубликатами
    def test_duplicates(self):
        # given
        arr = [3, 1, 2, 3, 1]
        merge_sort(arr, 0, len(arr) - 1, self.output)
        # when
        self.assertEqual(arr, [1, 1, 2, 3, 3])
        # then
        self.assertIn("1 5 1 3\n", self.output.getvalue())

if __name__ == "__main__":
    unittest.main()
