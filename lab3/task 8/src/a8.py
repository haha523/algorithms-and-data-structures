import sys
import heapq

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    with open(input_file, 'r') as f:
        n, k = map(int, f.readline().strip().split())
        points = [tuple(map(int, f.readline().strip().split())) for _ in range(n)]

    distances = []
    for x, y in points:
        distance_squared = x * x + y * y
        distances.append((distance_squared, (x, y)))

    distances.sort(key=lambda item: item[0])

    closest_points = [distances[i][1] for i in range(k)]

    result = [f"[{x},{y}]" for x, y in closest_points]
    output = ",".join(result)

    with open(output_file, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()