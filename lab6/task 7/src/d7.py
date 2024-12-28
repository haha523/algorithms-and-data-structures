import os
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        n, k = map(int, f.readline().strip().split())
        stones = f.readline().strip()
        pairs = [tuple(f.readline().strip()) for _ in range(k)]
    return n, k, stones, pairs

def write_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(str(result) + "\n")

def count_beautiful_pairs(n, stones, pairs):
    count = 0

    stone_count = defaultdict(int)

    for i in range(n):
        for a, b in pairs:
            if stones[i] == b:
                count += stone_count[a]
        stone_count[stones[i]] += 1

    return count

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    n, k, stones, pairs = read_input(input_path)
    result = count_beautiful_pairs(n, stones, pairs)
    write_output(output_path, result)

if __name__ == "__main__":
    main()
