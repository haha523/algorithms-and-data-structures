import os

def digital_sorting(n, m, k, data):
    strings = [''] * n
    for j in range(m):
        for i in range(n):
            strings[i] += data[j][i]

    indices = list(range(1, n + 1))

    for phase in range(1, k + 1):
        indices.sort(key=lambda x: strings[x - 1][m - phase])

    return indices

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as f:
        n, m, k = map(int, f.readline().strip().split())
        data = [f.readline().strip() for _ in range(m)]

    result = digital_sorting(n, m, k, data)

    with open(output_file_path, 'w') as f:
        f.write(' '.join(map(str, result)) + '\n')

if __name__ == "__main__":
    main()