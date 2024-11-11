def calculate_h_index(citations):
    citations.sort(reverse=True)

    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index

with open('input.txt', 'r') as f:
    line = f.readline().strip()
    citations = list(map(int, line.replace(',', ' ').split()))

h_index = calculate_h_index(citations)

with open('output.txt', 'w') as f:
    f.write(str(h_index) + '\n')