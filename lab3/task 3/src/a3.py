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
    with open("input.txt", "r") as file:
        n, k = map(int, file.readline().strip().split())
        sizes = list(map(int, file.readline().strip().split()))

    if can_sort_with_k(n, k, sizes):
        with open("output.txt", "w", encoding='utf-8') as file:
            file.write("ДА\n")
    else:
        with open("output.txt", "w", encoding='utf-8') as file:
            file.write("НЕТ\n")

if __name__ == "__main__":
    main()