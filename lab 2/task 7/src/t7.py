def max_subarray_kadane(arr):
    max_current = arr[0]
    max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        
        if max_current > max_global:
            max_global = max_current
    
    return max_global

def main():
    with open('d:/Visual studio code/lab_2.py/input for t7.txt', 'r') as file:
        arr = list(map(int, file.readline().split()))

    max_sum = max_subarray_kadane(arr)
    
    with open('d:/Visual studio code/lab_2.py/output for t7.txt', 'w') as file:
        file.write(f"Max Subarray Sum: {max_sum}\n")

if __name__ == "__main__":
    main()
