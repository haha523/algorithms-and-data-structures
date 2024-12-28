import tracemalloc
import time

def read_lines(file_path, num=-1, start=0, data_type=str):
    with open(file_path) as f:
        lines = f.readlines()[start:start + (num if num != -1 else None)]
        return [data_type(line.strip()) for line in lines]

def read_array(file_path, line=0, data_type=int):
    with open(file_path) as f:
        return [data_type(x) for x in f.readlines()[line].strip().split()]

def write_vars(file_path, *args, mode='w'):
    with open(file_path, mode) as fout:
        for item in args:
            if isinstance(item, (list, tuple)):
                fout.write(' '.join(map(str, item)) + '\n')
            else:
                fout.write(f'{item}\n')

def print_time_memory(task_func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()

        result = task_func(*args, **kwargs)

        memory_usage = tracemalloc.get_traced_memory()[1]
        elapsed_time = time.time() - start_time

        print(f"Memory usage: {memory_usage} bytes")
        print(f"--- {elapsed_time:.6f} seconds ---\n")

        tracemalloc.stop()
        return result
    return wrapper

def is_sorted(lst, reverse=False):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) if not reverse else all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
