import unittest

# Функция для нахождения максимальной подмассива, пересекающего середину
def max_crossing_subarray(prices_diff, low, mid, high):
    left_sum = float('-inf')  # Начальное значение для левой суммы
    sum = 0
    max_left = mid  # Индекс максимального элемента слева

    # Проходимся по левой части массива
    for i in range(mid, low - 1, -1):
        sum += prices_diff[i]
        if sum > left_sum:  # Если сумма больше, обновляем значения
            left_sum = sum
            max_left = i

    right_sum = float('-inf')  # Начальное значение для правой суммы
    sum = 0
    max_right = mid + 1  # Индекс максимального элемента справа

    # Проходимся по правой части массива
    for j in range(mid + 1, high + 1):
        sum += prices_diff[j]
        if sum > right_sum:  # Если сумма больше, обновляем значения
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum  # Возвращаем границы и сумму

# Функция для нахождения максимального подмассива
def max_subarray(prices_diff, low, high):
    if low == high:  # Базовый случай, когда подмассив состоит из одного элемента
        return low, high, prices_diff[low]

    mid = (low + high) // 2  # Находим середину
    left_low, left_high, left_sum = max_subarray(prices_diff, low, mid)  # Левый подмассив
    right_low, right_high, right_sum = max_subarray(prices_diff, mid + 1, high)  # Правый подмассив
    cross_low, cross_high, cross_sum = max_crossing_subarray(prices_diff, low, mid, high)  # Пересекающийся подмассив

    # Сравниваем суммы и возвращаем максимальную
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

# Функция для нахождения максимальной прибыли
def find_max_profit(prices):
    if not prices:  # Если список пустой
        return 1, 1, 0  # Возвращаем 0 прибыли

    # Рассчитываем разницу цен
    prices_diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

    if not prices_diff or all(diff <= 0 for diff in prices_diff):  # Если нет прибыли
        return 1, 1, 0  # Возвращаем 0 прибыли

    # Находим максимальную прибыль с помощью подмассива
    buy_day, sell_day, max_profit = max_subarray(prices_diff, 0, len(prices_diff) - 1)

    return buy_day + 1, sell_day + 1, max_profit  # Возвращаем дни покупки и продажи (с учетом индексации)

# Класс для тестирования функции нахождения максимальной прибыли
class TestMaxProfit(unittest.TestCase):
    def test_basic_profit(self):
        # given
        prices = [100, 180, 260, 310, 40, 535, 695]
        # when
        buy_day, sell_day, max_profit = find_max_profit(prices)
        # then
        self.assertEqual((buy_day, sell_day, max_profit), (5, 6, 655))

    def test_no_profit(self):
        # given
        prices = [90, 80, 70, 60, 50]
        # when
        buy_day, sell_day, max_profit = find_max_profit(prices)
        # then
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_single_day(self):
        # given
        prices = [100]
        # when
        buy_day, sell_day, max_profit = find_max_profit(prices)
        # then
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_empty_prices(self):
        # given
        prices = []
        # when
        buy_day, sell_day, max_profit = find_max_profit(prices)
        # then
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_profit_with_same_prices(self):
        # given
        prices = [100, 100, 100, 100]
        # when
        buy_day, sell_day, max_profit = find_max_profit(prices)
        # then
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_multiple_peak_and_valley(self):
        # given
        prices = [100, 200, 150, 300, 250, 400]
        # when
        buy_day, sell_day, max_profit = find_max_profit(prices)
        # then
        self.assertEqual((buy_day, sell_day, max_profit), (1, 5, 300))

if __name__ == "__main__":
    unittest.main()