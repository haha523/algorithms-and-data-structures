import heapq
import os

def task_scheduler(input_file='input.txt', output_file='output.txt'):
    input_path = os.path.join('..', 'txtf', input_file)
    output_path = os.path.join('..', 'txtf', output_file)

    with open(input_path, 'r') as f:
        n, m = map(int, f.readline().strip().split())
        tasks = list(map(int, f.readline().strip().split()))

    min_heap = []
    for i in range(n):
        heapq.heappush(min_heap, (0, i))

    results = []

    for task_time in tasks:
        finish_time, thread_index = heapq.heappop(min_heap)

        results.append((thread_index, finish_time))

        new_finish_time = finish_time + task_time

        heapq.heappush(min_heap, (new_finish_time, thread_index))

    with open(output_path, 'w') as f:
        for thread_index, start_time in results:
            f.write(f"{thread_index} {start_time}\n")

if __name__ == "__main__":
    task_scheduler()
