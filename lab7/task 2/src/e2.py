import os
from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
    return n

def write_output(file_path, k, sequence):
    with open(file_path, 'w') as f:
        f.write(f"{k}\n")
        f.write(" ".join(map(str, sequence)) + "\n")

def optimal_sequence(n):
    queue = deque([1])
    parents = {1: None}
    operations_count = {1: 0}

    while queue:
        current = queue.popleft()

        if current == n:
            break

        for next_value in (current * 2, current * 3, current + 1):
            if next_value <= n and next_value not in parents:
                parents[next_value] = current
                operations_count[next_value] = operations_count[current] + 1
                queue.append(next_value)

    sequence = []
    while n is not None:
        sequence.append(n)
        n = parents[n]

    sequence.reverse()
    return operations_count[sequence[-1]], sequence

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    n = read_input(input_path)
    k, sequence = optimal_sequence(n)
    write_output(output_path, k, sequence)

if __name__ == "__main__":
    main()
