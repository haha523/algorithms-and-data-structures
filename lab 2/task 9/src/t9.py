import numpy as np 

def simple_matrix_multiplication(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C
def add_matrix(A, B):
    n = len(A)
    result = [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]
    return result

def sub_matrix(A, B):
    n = len(A)
    result = [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
    return result

def strassen_multiplication(A, B):
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2

    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]

    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    P1 = strassen_multiplication(add_matrix(A11, A22), add_matrix(B11, B22))
    P2 = strassen_multiplication(add_matrix(A21, A22), B11)
    P3 = strassen_multiplication(A11, sub_matrix(B12, B22))
    P4 = strassen_multiplication(A22, sub_matrix(B21, B11))
    P5 = strassen_multiplication(add_matrix(A11, A12), B22)
    P6 = strassen_multiplication(sub_matrix(A21, A11), add_matrix(B11, B12))
    P7 = strassen_multiplication(sub_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(sub_matrix(add_matrix(P1, P4), P5), P7)
    C12 = add_matrix(P3, P5)
    C21 = add_matrix(P2, P4)
    C22 = add_matrix(sub_matrix(add_matrix(P1, P3), P2), P6)

    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j+mid] = C12[i][j]
            C[i+mid][j] = C21[i][j]
            C[i+mid][j+mid] = C22[i][j]

    return C
def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0].strip())
    matrix_A = []
    matrix_B = []
    
    for i in range(1, n+1):
        matrix_A.append(list(map(int, lines[i].strip().split())))
    for i in range(n+1, 2*n+1):
        matrix_B.append(list(map(int, lines[i].strip().split())))
    
    return n, matrix_A, matrix_B

def write_output(filename, matrix):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

if __name__ == '__main__':
    n, A, B = read_input('d:/Visual studio code/lab_2.py/input for t9.txt')
    
    result_simple = simple_matrix_multiplication(A, B)
    write_output('d:/Visual studio code/lab_2.py/output_simple for t9.txt', result_simple)
    
    result_strassen = strassen_multiplication(A, B)
    write_output('d:/Visual studio code/lab_2.py/output_strassen for t9.txt', result_strassen)
