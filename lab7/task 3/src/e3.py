import os

def read_input(file_path):
    with open(file_path, 'r') as f:
        str1 = f.readline().strip()
        str2 = f.readline().strip()
    return str1, str2

def write_output(file_path, distance):
    with open(file_path, 'w') as f:
        f.write(f"{distance}\n")

def edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + 1)

    return dp[len1][len2]

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    str1, str2 = read_input(input_path)
    distance = edit_distance(str1, str2)
    write_output(output_path, distance)

if __name__ == "__main__":
    main()
