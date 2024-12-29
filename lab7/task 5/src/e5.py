import os

def read_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        sequence_a = list(map(int, f.readline().strip().split()))
        m = int(f.readline().strip())
        sequence_b = list(map(int, f.readline().strip().split()))
        l = int(f.readline().strip())
        sequence_c = list(map(int, f.readline().strip().split()))
    return sequence_a, sequence_b, sequence_c

def write_output(file_path, length):
    with open(file_path, 'w') as f:
        f.write(f"{length}\n")

def lcs_length(sequence_a, sequence_b, sequence_c):
    n = len(sequence_a)
    m = len(sequence_b)
    l = len(sequence_c)

    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if sequence_a[i - 1] == sequence_b[j - 1] == sequence_c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    sequence_a, sequence_b, sequence_c = read_input(input_path)
    length = lcs_length(sequence_a, sequence_b, sequence_c)
    write_output(output_path, length)

if __name__ == "__main__":
    main()
