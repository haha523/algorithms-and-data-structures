from collections import deque

def max_in_sliding_window(n, arr, m):
    result = []
    deq = deque()

    for i in range(n):
        if deq and deq[0] < i - m + 1:
            deq.popleft()

        while deq and arr[deq[-1]] < arr[i]:
            deq.pop()

        deq.append(i)

        if i >= m - 1:
            result.append(arr[deq[0]])

    return result

def main():
    input_file_path = '../txtf/input.txt'
    output_file_path = '../txtf/output.txt'

    with open(input_file_path, 'r', encoding='utf-8') as infile:
        n = int(infile.readline().strip())  # Read n
        arr = list(map(int, infile.readline().strip().split()))  # Read array
        m = int(infile.readline().strip())  # Read m

    result = max_in_sliding_window(n, arr, m)

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(' '.join(map(str, result)) + '\n')

if __name__ == '__main__':
    main()