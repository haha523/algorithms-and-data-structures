import unittest


def poly_multiply(A, B):
    n = len(A)
    m = len(B)

    if n == 0 or m == 0:
        return []

    if n == 1 and m == 1:
        return [A[0] * B[0]]

    if n == 1:
        return [A[0] * b for b in B]

    if m == 1:
        return [B[0] * a for a in A]

    mid = n // 2
    A_low = A[:mid]
    A_high = A[mid:]
    B_low = B[:mid]
    B_high = B[mid:]

    z0 = poly_multiply(A_low, B_low)
    z2 = poly_multiply(A_high, B_high)

    A_sum = [a + b for a, b in zip(A_low + [0] * (len(A_high) - len(A_low)), A_high)]
    B_sum = [a + b for a, b in zip(B_low + [0] * (len(B_high) - len(B_low)), B_high)]

    z1 = poly_multiply(A_sum, B_sum)

    max_length = max(len(z1), len(z0), len(z2))
    z1 += [0] * (max_length - len(z1))
    z0 += [0] * (max_length - len(z0))
    z2 += [0] * (max_length - len(z2))

    z1 = [z1[i] - z0[i] - z2[i] for i in range(max_length)]

    result = [0] * (n + m - 1)

    for i in range(len(z0)):
        result[i] += z0[i]

    for i in range(len(z1)):
        result[i + mid] += z1[i]

    for i in range(len(z2)):
        result[i + 2 * mid] += z2[i]

    return result

class TestPolyMultiply(unittest.TestCase):

    def test_simple_polynomials(self):
        A = [1, 2]  # 1 + 2x
        B = [3, 4]  # 3 + 4x
        expected = [3, 10, 8]  # 3 + 10x + 8x^2
        self.assertEqual(poly_multiply(A, B), expected)

    def test_polynomials_of_different_degrees(self):
        A = [1, 0, 2]  # 1 + 0x + 2x^2
        B = [3, 4]  # 3 + 4x
        expected = [3, 4, 6, 8]  # 3 + 4x + 6x^2 + 8x^3
        self.assertEqual(poly_multiply(A, B), expected)

    def test_zero_polynomial(self):
        A = [0, 0]  # 0 + 0x
        B = [1, 1]  # 1 + 1x
        expected = [0, 0, 0]  # 0
        self.assertEqual(poly_multiply(A, B), expected)

    def test_same_degree_polynomials(self):
        A = [1, 2, 3]  # 1 + 2x + 3x^2
        B = [4, 5, 6]

if __name__ == "__main__":
    unittest.main()
