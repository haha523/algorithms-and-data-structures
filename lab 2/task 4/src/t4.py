def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  

def main():
    with open('d:/Visual studio code/lab_2.py/input for t4.txt', 'r') as file:
        n = int(file.readline().strip())
        a = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        b = list(map(int, file.readline().strip().split()))

    result = []
    for number in b:
        index = binary_search(a, number)
        result.append(index)
        
    with open('d:/Visual studio code/lab_2.py/output for t4.txt', 'w') as file:
        file.write(' '.join(map(str, result)) + '\n')

if __name__ == '__main__':
    main()
