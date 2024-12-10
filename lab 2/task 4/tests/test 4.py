import unittest

# Функция бинарного поиска для нахождения первого вхождения элемента
def binary_search_first_occurrence(arr, x):
    left, right = 0, len(arr) - 1  # Устанавливаем границы поиска
    result = -1  # Изначально результат не найден

    while left <= right:  # Пока границы не пересеклись
        mid = (left + right) // 2  # Находим середину

        if arr[mid] == x:  # Если элемент найден
            result = mid  # Сохраняем индекс
            right = mid - 1  # Продолжаем искать в левой части
        elif arr[mid] < x:  # Если элемент в середине меньше искомого
            left = mid + 1  # Ищем в правой части
        else:  # Если элемент в середине больше искомого
            right = mid - 1  # Ищем в левой части

    return result  # Возвращаем индекс первого вхождения или -1, если не найден

# Класс для тестирования бинарного поиска
class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 3), 2)

    def test_element_not_found(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 6), -1)

    def test_first_element(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 1), 0)

    def test_last_element(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 5), 4)

    def test_empty_array(self):
        # given
        arr = []
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 1), -1)

    def test_single_element_found(self):
        # given
        arr = [42]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 42), 0)

    def test_single_element_not_found(self):
        # given
        arr = [42]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 0), -1)

    def test_multiple_occurrences(self):
        # given
        arr = [1, 2, 2, 2, 3]
        # then
        self.assertEqual(binary_search_first_occurrence(arr, 2), 1)

if __name__ == '__main__':
    unittest.main()
