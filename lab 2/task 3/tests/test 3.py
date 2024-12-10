import unittest

# Функция для слияния двух подмассивов и подсчета инверсий
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left  # Индекс для левой части
    j = mid + 1  # Индекс для правой части
    k = left  # Индекс для временного массива
    inv_count = 0  # Счетчик инверсий

    # Слияние двух подмассивов
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:  # Если элемент из левой части меньше или равен элементу из правой
            temp_arr[k] = arr[i]  # Копируем в временный массив
            i += 1
        else:
            temp_arr[k] = arr[j]  # Копируем элемент из правой части
            inv_count += (mid - i + 1)  # Увеличиваем счетчик инверсий
            j += 1
        k += 1

    # Копируем оставшиеся элементы из левой части
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из правой части
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Копируем временные элементы обратно в оригинальный массив
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count  # Возвращаем количество инверсий

# Функция сортировки слиянием с подсчетом инверсий
def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0  # Инициализируем счетчик инверсий
    if left < right:  # Если в подмассиве больше одного элемента
        mid = (left + right) // 2  # Находим середину

        # Рекурсивно сортируем и подсчитываем инверсии для левой и правой частей
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        # Сливаем и подсчитываем инверсии
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count  # Возвращаем общее количество инверсий

# Функция для подсчета инверсий в массиве
def count_inversions(arr):
    temp_arr = [0] * len(arr)  # Создаем временный массив
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)  # Запускаем сортировку и подсчет инверсий

# Класс для тестирования подсчета инверсий
class TestInversionCount(unittest.TestCase):
    def test_no_inversions(self):
        # given
        arr = [1, 2, 3, 4, 5]
        # then
        self.assertEqual(count_inversions(arr), 0)

    def test_some_inversions(self):
        # given
        arr = [2, 3, 8, 6, 1]
        # then
        self.assertEqual(count_inversions(arr), 5)
    def test_all_inversions(self):
        # given
        arr = [5, 4, 3, 2, 1]
        # then
        self.assertEqual(count_inversions(arr), 10)

    def test_empty_array(self):
        # given
        arr = []
        # then
        self.assertEqual(count_inversions(arr), 0)

    def test_single_element_array(self):
        # given
        arr = [42]
        # then
        self.assertEqual(count_inversions(arr), 0)

    def test_duplicates(self):
        # given
        arr = [1, 3, 2, 3, 1]
        # then
        self.assertEqual(count_inversions(arr), 4)

if __name__ == "__main__":
    unittest.main()
