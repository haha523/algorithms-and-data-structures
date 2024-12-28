import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from d2 import PhoneBook

class TestPhoneBook(unittest.TestCase):

    def test_operations(self):
        # given
        operations = [
            "add 911 police",
            "add 76213 Mom",
            "add 17239 Bob",
            "find 76213",
            "find 910",
            "find 911",
            "del 910",
            "del 911",
            "find 911",
            "find 76213",
            "add 76213 daddy",
            "find 76213"
        ]
        expected_output = [
            "Mom",
            "not found",
            "police",
            "not found",
            "Mom",
            "daddy"
        ]

        # when
        phone_book = PhoneBook()
        results = []

        # when
        for operation in operations:
            parts = operation.split()
            cmd = parts[0]
            if cmd == 'add':
                number = parts[1]
                name = parts[2]
                phone_book.add(number, name)
            elif cmd == 'del':
                number = parts[1]
                phone_book.delete(number)
            elif cmd == 'find':
                number = parts[1]
                result = phone_book.find(number)
                results.append(result)

        # then
        self.assertEqual(results, expected_output)

if __name__ == "__main__":
    unittest.main()
