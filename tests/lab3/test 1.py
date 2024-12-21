import time
import os
from src.lab3.sudoku import read_sudoku, solve

def read_sudoku(file_path):
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            grid.append(line.strip().split())
    return grid

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        grid = read_sudoku(filename)
        start = time.time()
        solve(grid)
        end = time.time()
        print(f"{filename}: {end - start} seconds")