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

    prices_diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

    buy_day, sell_day, max_profit = max_subarray(prices_diff, 0, len(prices_diff) - 1)

    return buy_day + 1, sell_day + 1, max_profit

def main():
    with open('d:/Visual studio code/lab_2.py/input for t6.txt', 'r') as file:
        company_name = file.readline().strip()
        dates = file.readline().strip().split()
        prices = list(map(float, file.readline().strip().split()))

    buy_day, sell_day, max_profit = find_max_profit(prices)

    with open('d:/Visual studio code/lab_2.py/output for t6.txt', 'w') as file:
        file.write(f"Company: {company_name}\n")
        file.write(f"Buy on: {dates[buy_day]}\n")
        file.write(f"Sell on: {dates[sell_day]}\n")
        file.write(f"Max Profit: {max_profit}\n")

if __name__ == "__main__":
    main()
