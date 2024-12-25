import os

def can_sort_with_k(n, k, sizes):
    groups = [[] for _ in range(k)]

    for i in range(n):
        groups[i % k].append(sizes[i])

    for group in groups:
        group.sort()

    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])

    return sorted_sizes == sorted(sizes)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, "r") as file:
        n, k = map(int, file.readline().strip().split())
        sizes = list(map(int, file.readline().strip().split()))

    if can_sort_with_k(n, k, sizes):
        with open(output_file_path, "w", encoding='utf-8') as file:
            file.write("ДА\n")
    else:
        with open(output_file_path, "w", encoding='utf-8') as file:
            file.write("НЕТ\n")

if __name__ == "__main__":
    main()