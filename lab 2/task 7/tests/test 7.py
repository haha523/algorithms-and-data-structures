import unittest
from io import StringIO
import sys

# Функция для нахождения максимальной суммы подмассива с помощью алгоритма Кадане
def max_subarray_kadane(arr):
    max_current = arr[0]  # Начальная сумма текущего подмассива
    max_global = arr[0]   # Начальная максимальная сумма подмассива

    # Проходимся по массиву начиная со второго элемента
    for i in range(1, len(arr)):
        # Обновляем текущую максимальную сумму
        max_current = max(arr[i], max_current + arr[i])  # Сравниваем текущий элемент и сумму с ним
        # Если текущая сумма больше глобальной, обновляем глобальную
        if max_current > max_global:
            max_global = max_current

    return max_global  # Возвращаем максимальную сумму подмассива

# Класс для тестирования функции максимальной суммы подмассива
class TestMaxSubarrayKadane(unittest.TestCase):

    def test_positive_numbers(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(max_subarray_kadane(arr), 15)

    def test_negative_numbers(self):
        # given
        arr = [-1, -2, -3, -4]
        # then
        self.assertEqual(max_subarray_kadane(arr), -1)

    def test_mixed_numbers(self):
        # given
        arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
        # then
        self.assertEqual(max_subarray_kadane(arr), 9)

    def test_all_zeroes(self):
        # given
        arr = [0, 0, 0, 0]
        # then
        self.assertEqual(max_subarray_kadane(arr), 0)

    def test_single_element(self):
        # given
        arr = [42]
        # then
        self.assertEqual(max_subarray_kadane(arr), 42)

    def test_alternating_signs(self):
        # given
        arr = [5, -1, 2, -1, 3]
        # then
        self.assertEqual(max_subarray_kadane(arr), 8)

    def test_numbers(self):
        # given
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        # then
        self.assertEqual(max_subarray_kadane(arr), 6)

if __name__ == "__main__":
    unittest.main()
