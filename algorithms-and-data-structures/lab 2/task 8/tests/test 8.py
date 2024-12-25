import unittest

# Функция для умножения двух полиномов, представленных списками коэффициентов
def poly_multiply(A, B):
    n = len(A)    # Длина полинома A
    m = len(B)    # Длина полинома B

    if n == 0 or m == 0:   # Если один из полиномов пустой
        return []

    if n == 1 and m == 1:   # Если оба полинома имеют только один коэффициент
        return [A[0] * B[0]]

    if n == 1:    # Если полином A имеет один коэффициент
        return [A[0] * b for b in B]

    if m == 1:    # Если полином B имеет один коэффициент
        return [B[0] * a for a in A]

    mid = n // 2    # Находим середину полинома A
    A_low = A[:mid]    # Нижняя половина A
    A_high = A[mid:]    # Верхняя половина A
    B_low = B[:mid]    # Нижняя половина B
    B_high = B[mid:]    # Верхняя половина B

    z0 = poly_multiply(A_low, B_low)    # Умножение нижних половин
    z2 = poly_multiply(A_high, B_high)    # Умножение верхних половин

    # Суммируем верхние и нижние половины A и B
    A_sum = [a + b for a, b in zip(A_low + [0] * (len(A_high) - len(A_low)), A_high)]
    B_sum = [a + b for a, b in zip(B_low + [0] * (len(B_high) - len(B_low)), B_high)]

    z1 = poly_multiply(A_sum, B_sum)    # Умножение сумм

    max_length = max(len(z1), len(z0), len(z2))    # Максимальная длина результата
    z1 += [0] * (max_length - len(z1))    # Дополняем нулями до максимальной длины
    z0 += [0] * (max_length - len(z0))
    z2 += [0] * (max_length - len(z2))

    z1 = [z1[i] - z0[i] - z2[i] for i in range(max_length)]    # Вычисляем z1

    result = [0] * (n + m - 1)    # Результирующий полином

    # Суммируем результаты
    for i in range(len(z0)):
        result[i] += z0[i]

    for i in range(len(z1)):
        result[i + mid] += z1[i]

    for i in range(len(z2)):
        result[i + 2 * mid] += z2[i]

    return result    # Возвращаем результирующий полином

# Класс для тестирования функции умножения полиномов
class TestPolyMultiply(unittest.TestCase):

    def test_simple_polynomials(self):
        # given
        A = [1, 2]
        B = [3, 4]
        # when
        expected = [3, 10, 8]
        # then
        self.assertEqual(poly_multiply(A, B), expected)

    def test_polynomials_of_different_degrees(self):
        # given
        A = [1, 0, 2]
        B = [3, 4]
        # when
        expected = [3, 4, 6, 8]
        # then
        self.assertEqual(poly_multiply(A, B), expected)

    def test_zero_polynomial(self):
        # given
        A = [0, 0]
        B = [1, 1]
        # when
        expected = [0, 0, 0]
        # then
        self.assertEqual(poly_multiply(A, B), expected)

    def test_same_degree_polynomials(self):
        # given
        A = [1, 2, 3]
        B = [4, 5, 6]
        # when
        expected = [4, 13, 28, 30, 18]

if __name__ == "__main__":
    unittest.main()
