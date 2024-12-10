import unittest

def read_input(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().strip().split())
        A = list(map(int, file.readline().strip().split()))
        B = list(map(int, file.readline().strip().split()))
    return n, m, A, B

def calculate_products(A, B):
    products = []
    for a in A:
        for b in B:
            products.append(a * b)
    return products

def calculate_sum_of_selected_products(A, B):
    products = calculate_products(A, B)
    products.sort()

    if len(products) >= 11:
        return products[0] + products[10]
    else:
        return sum(products)

class TestProductSum(unittest.TestCase):

    def test_example_case(self):
        # given
        A = [7, 1, 4, 9]
        B = [2, 7, 8, 11]
        expected_sum = 51
        # when
        result = calculate_sum_of_selected_products(A, B)
        # then
        self.assertEqual(result, expected_sum)

    def test_edge_case(self):
        # given
        A = [0, 0, 0, 0]
        B = [0, 0, 0, 0]
        expected_sum = 0
        # when
        result = calculate_sum_of_selected_products(A, B)
        # then
        self.assertEqual(result, expected_sum)

    def test_single_element(self):
        # given
        A = [1]
        B = [1]
        expected_sum = 1
        # when
        result = calculate_sum_of_selected_products(A, B)
        # then
        self.assertEqual(result, expected_sum)

    def test_large_elements(self):
        # given
        A = [40000, 40000, 40000, 40000]
        B = [40000, 40000, 40000, 40000]
        expected_sum = 3200000000
        # when
        result = calculate_sum_of_selected_products(A, B)
        # then
        self.assertEqual(result, expected_sum)

if __name__ == "__main__":
    unittest.main()