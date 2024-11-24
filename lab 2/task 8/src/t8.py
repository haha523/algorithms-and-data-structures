import os


def poly_multiply(A, B):
    n = len(A)

    if n == 1:
        return [A[0] * B[0]]

    mid = n // 2
    A_low = A[:mid]
    A_high = A[mid:]
    B_low = B[:mid]
    B_high = B[mid:]

    z0 = poly_multiply(A_low, B_low)
    z2 = poly_multiply(A_high, B_high)

    A_sum = [a + b for a, b in zip(A_low, A_high)]
    B_sum = [a + b for a, b in zip(B_low, B_high)]

    z1 = poly_multiply(A_sum, B_sum)

    z1 = [z1[i] - z0[i] - z2[i] for i in range(len(z1))]

    result = [0] * (2 * n - 1)

    for i in range(len(z0)):
        result[i] += z0[i]

    for i in range(len(z1)):
        result[i + mid] += z1[i]

    for i in range(len(z2)):
        result[i + 2 * mid] += z2[i]

    return result


def main():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as f:
        n = int(f.readline())
        A = list(map(int, f.readline().split()))
        B = list(map(int, f.readline().split()))

    C = poly_multiply(A, B)

    with open(output_file_path, 'w') as f:
        f.write(' '.join(map(str, C)))


if __name__ == "__main__":
    main()
