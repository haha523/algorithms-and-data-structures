def digital_sorting(n, m, k, data):
    strings = [''] * n
    for j in range(m):
        for i in range(n):
            strings[i] += data[j][i]

    indices = list(range(1, n + 1))

    for phase in range(1, k + 1):
        indices.sort(key=lambda x: strings[x - 1][m - phase])

    return indices

with open('input.txt', 'r') as f:
    n, m, k = map(int, f.readline().strip().split())
    data = [f.readline().strip() for _ in range(m)]

result = digital_sorting(n, m, k, data)

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, result)) + '\n')