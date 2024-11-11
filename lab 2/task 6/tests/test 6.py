import unittest

def max_crossing_subarray(prices_diff, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        sum += prices_diff[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1

    for j in range(mid + 1, high + 1):
        sum += prices_diff[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

def max_subarray(prices_diff, low, high):
    if low == high:
        return low, high, prices_diff[low]

    mid = (low + high) // 2
    left_low, left_high, left_sum = max_subarray(prices_diff, low, mid)
    right_low, right_high, right_sum = max_subarray(prices_diff, mid + 1, high)
    cross_low, cross_high, cross_sum = max_crossing_subarray(prices_diff, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def find_max_profit(prices):
    if not prices:
        return 1, 1, 0  # Trả về cho trường hợp danh sách rỗng

    prices_diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

    if not prices_diff or all(diff <= 0 for diff in prices_diff):
        return 1, 1, 0  # Trả về cho trường hợp không có lợi nhuận

    buy_day, sell_day, max_profit = max_subarray(prices_diff, 0, len(prices_diff) - 1)

    return buy_day + 1, sell_day + 1, max_profit

class TestMaxProfit(unittest.TestCase):
    def test_basic_profit(self):
        prices = [100, 180, 260, 310, 40, 535, 695]
        buy_day, sell_day, max_profit = find_max_profit(prices)
        self.assertEqual((buy_day, sell_day, max_profit), (5, 6, 655))

    def test_no_profit(self):
        prices = [90, 80, 70, 60, 50]
        buy_day, sell_day, max_profit = find_max_profit(prices)
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_single_day(self):
        prices = [100]
        buy_day, sell_day, max_profit = find_max_profit(prices)
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_empty_prices(self):
        prices = []
        buy_day, sell_day, max_profit = find_max_profit(prices)
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_profit_with_same_prices(self):
        prices = [100, 100, 100, 100]
        buy_day, sell_day, max_profit = find_max_profit(prices)
        self.assertEqual((buy_day, sell_day, max_profit), (1, 1, 0))

    def test_multiple_peak_and_valley(self):
        prices = [100, 200, 150, 300, 250, 400]
        buy_day, sell_day, max_profit = find_max_profit(prices)
        self.assertEqual((buy_day, sell_day, max_profit), (1, 5, 300))

if __name__ == "__main__":
    unittest.main()