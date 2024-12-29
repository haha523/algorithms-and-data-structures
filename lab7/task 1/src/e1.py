import os

def read_input(file_path):
    with open(file_path, 'r') as f:
        money, k = map(int, f.readline().strip().split())
        coins = list(map(int, f.readline().strip().split()))
    return money, coins

def write_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(str(result) + "\n")

def min_coins(money, coins):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, money + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    money, coins = read_input(input_path)
    result = min_coins(money, coins)
    write_output(output_path, result)

if __name__ == "__main__":
    main()
