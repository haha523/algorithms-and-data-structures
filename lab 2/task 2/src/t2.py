import os

def merge(arr, left, mid, right, output):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    output.write(f"{left + 1} {right + 1} {arr[left]} {arr[right]}\n")

def merge_sort(arr, left, right, output):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid, output)
        merge_sort(arr, mid + 1, right, output)

        merge(arr, left, mid, right, output)

def main():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    if not os.path.exists(input_file_path):
        print(f"File does not exist: {input_file_path}")
        return

    with open(input_file_path, 'r') as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    with open(output_file_path, 'w') as output:
        merge_sort(arr, 0, n - 1, output)
        output.write(" ".join(map(str, arr)) + "\n")

if __name__ == "__main__":
    main()
