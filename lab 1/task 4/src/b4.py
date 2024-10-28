def linear_search(arr, v):
    indices = [i for i, x in enumerate(arr) if x == v]
    
    if len(indices) > 0:
        return f"{len(indices)}: " + ', '.join(map(str, indices))
    else:
        return "-1"

with open('d:/Visual studio code/lab_1.py/input for b4.txt', 'r') as file:
    arr = list(map(int, file.readline().split()))
    v = int(file.readline().strip())

result = linear_search(arr, v)

with open('d:/Visual studio code/lab_1.py/output for b4.txt', 'w') as file:
    file.write(result)
