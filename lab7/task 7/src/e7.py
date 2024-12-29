import os

def read_input(file_path):
    with open(file_path, 'r') as f:
        pattern = f.readline().strip()
        string = f.readline().strip()
    return pattern, string

def write_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(result + '\n')


def is_match(pattern, string):
    m, n = len(pattern), len(string)

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    pattern, string = read_input(input_path)
    if is_match(pattern, string):
        write_output(output_path, "YES")
    else:
        write_output(output_path, "NO")

if __name__ == "__main__":
    main()
