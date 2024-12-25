def is_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return "NO"

        if right < n and arr[i] > arr[right]:
            return "NO"

    return "YES"

input_file_path = '../txtf/input.txt'
output_file_path = '../txtf/output.txt'

with open(input_file_path) as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

result = is_min_heap(arr)

with open(output_file_path, 'w') as f:
    f.write(result)