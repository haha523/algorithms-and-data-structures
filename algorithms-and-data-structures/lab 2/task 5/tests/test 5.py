import unittest

# Функция для подсчета количества вхождений кандидата в массив
def count_occurrences(array, candidate):
    return sum(1 for x in array if x == candidate)

# Рекурсивная функция для нахождения большинства при помощи алгоритма "разделяй и властвуй"
def majority_element(array, left, right):
    # Если границы неверные, возвращаем None
    if left > right:
        return None

    # Если границы совпадают, возвращаем элемент
    if left == right:
        return array[left]

    # Находим середину массива
    mid = (left + right) // 2
    left_candidate = majority_element(array, left, mid)
    right_candidate = majority_element(array, mid + 1, right)

    # Если кандидаты совпадают, возвращаем этого кандидата
    if left_candidate == right_candidate:
        return left_candidate

    # Подсчитываем количество вхождений каждого кандидата
    left_count = count_occurrences(array, left_candidate)
    right_count = count_occurrences(array, right_candidate)

    # Возвращаем кандидата с большим количеством вхождений
    return left_candidate if left_count > right_count else right_candidate

# Функция для поиска большинства в массиве
def find_majority(n, array):
    # Если массив пустой, возвращаем 0
    if n == 0:
        return 0

    # Находим кандидата для большинства
    candidate = majority_element(array, 0, n - 1)
    # Проверяем, является ли кандидат действительным
    if candidate is not None and count_occurrences(array, candidate) > n // 2:
        return 1
    return 0

# Класс для тестирования функций
class TestMajorityElement(unittest.TestCase):
    def test_majority_exists(self):
        # given
        arr = [1, 2, 3, 2, 2]
        # then
        self.assertEqual(find_majority(len(arr), arr), 1)

    def test_majority_not_exists(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(find_majority(len(arr), arr), 0)

    def test_empty_array(self):
        # given
        arr = []
        # then
        self.assertEqual(find_majority(len(arr), arr), 0)

    def test_single_element_majority(self):
        # given
        arr = [42]
        # then
        self.assertEqual(find_majority(len(arr), arr), 1)

    def test_single_element_no_majority(self):
        # given
        arr = [1, 1, 2, 2, 3]
        # then
        self.assertEqual(find_majority(len(arr), arr), 0)

    def test_multiple_occurrences(self):
        # given
        arr = [1, 1, 1, 2, 2, 2, 1]
        # then
        self.assertEqual(find_majority(len(arr), arr), 1)

if __name__ == "__main__":
    unittest.main()