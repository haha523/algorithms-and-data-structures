import os

def read_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        sequence = list(map(int, f.readline().strip().split()))
    return n, sequence

def write_output(file_path, length, subsequence):
    with open(file_path, 'w') as f:
        f.write(f"{length}\n")
        f.write(" ".join(map(str, subsequence)) + "\n")

def longest_increasing_subsequence(sequence):
    n = len(sequence)
    if n == 0:
        return 0, []

    lis_length = [1] * n
    previous_index = [-1] * n
    max_length = 0
    max_index = 0

    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j] and lis_length[i] < lis_length[j] + 1:
                lis_length[i] = lis_length[j] + 1
                previous_index[i] = j

        if lis_length[i] > max_length:
            max_length = lis_length[i]
            max_index = i

    lis = []
    while max_index != -1:
        lis.append(sequence[max_index])
        max_index = previous_index[max_index]

    lis.reverse()
    return max_length, lis

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    n, sequence = read_input(input_path)
    length, subsequence = longest_increasing_subsequence(sequence)
    write_output(output_path, length, subsequence)

if __name__ == "__main__":
    main()
