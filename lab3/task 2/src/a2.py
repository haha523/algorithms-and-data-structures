def generate_anti_quick_sort(n):
    result = []
    for i in range(1, n + 1, 2):
        result.append(i)
    for i in range(2, n + 1, 2):
        result.append(i)

    return result

with open("input.txt", "r") as file:
    n = int(file.readline().strip())

anti_quick_sort_array = generate_anti_quick_sort(n)

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, anti_quick_sort_array)))