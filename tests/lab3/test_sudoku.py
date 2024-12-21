import pathlib
import unittest
from src.lab3.sudoku import group, get_row, get_col, get_block, read_sudoku
import sys
sys.path.append('c:/Users/FPT 2633/cs102/src')
import os
print(os.getcwd())

def read_puzzle(file_path: str) -> list:
    path = (pathlib.Path(__file__).parent / f'../../src/lab3/{file_path}')
    return read_sudoku(path)

class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_row(self):
        grid = read_puzzle('puzzle1.txt')
        self.assertEqual(get_row(grid, (0, 0)), ['5', '3', '.', '.', '7', '.', '.', '.', '.'])
        self.assertEqual(get_row(grid, (1, 0)), ['6', '.', '.', '1', '9', '5', '.', '.', '.'])

    def test_get_col(self):
        grid = read_puzzle('puzzle2.txt')
        self.assertEqual(get_col(grid, (0, 0)), ['.', '.', '.', '.', '.', '.', '.', '.', '.'])
        self.assertEqual(get_col(grid, (0, 1)), ['9', '.', '.', '8', '3', '.', '.', '.', '.'])

    def test_get_block(self):
        grid = read_puzzle('puzzle3.txt')
        self.assertEqual(get_block(grid, (0, 1)), ['8', '.', '.', '.', '.', '.', '.', '1', '.'])
        self.assertEqual(get_block(grid, (4, 7)), ['7', '8', '.', '.', '.', '.', '1', '.', '3'])

if __name__ == "__main__":
    unittest.main()