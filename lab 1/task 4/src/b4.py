def linear_search(arr, v):
    indices = [i for i, x in enumerate(arr) if x == v]
    
    if len(indices) > 0:
        return f"{len(indices)}: " + ', '.join(map(str, indices))
    else:
        return "-1"

with open('input.txt', 'r') as file:
    arr = list(map(int, file.readline().split()))
    v = int(file.readline().strip())

result = linear_search(arr, v)

with open('output.txt', 'w') as file:
    file.write(result)
