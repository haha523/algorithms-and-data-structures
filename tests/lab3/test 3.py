import multiprocessing
from src.lab3.sudoku import run_solve

if __name__ == "__main__":
    for filename in ("puzzle1.txt", "puzzle2.txt", "puzzle3.txt"):
        p = multiprocessing.Process(target=run_solve, args=(filename,))
        p.start()

import sys
print(sys.path)