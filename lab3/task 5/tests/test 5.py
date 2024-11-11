import unittest

def calculate_h_index(citations):
    citations.sort(reverse=True)

    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index


class TestCalculateHIndex(unittest.TestCase):

    def test_case_1(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        result = calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_case_2(self):
        citations = [1, 3, 1]
        expected = 1
        result = calculate_h_index(citations)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()