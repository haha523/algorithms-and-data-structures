import threading
import time

def read_sudoku(filename: str):
    with open(filename, 'r') as file:
        grid = []
        for line in file:
            grid.append([int(num) for num in line.split()])
    return grid

def solve(grid):
    pass

def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{filename}: {end - start:.4f} seconds")

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        t = threading.Thread(target=run_solve, args=(filename,))
        t.start()