import os

def count_segments_containing_points(segments, points):
    events = []

    for a, b in segments:
        events.append((a, 'start'))
        events.append((b, 'end'))

    for i, x in enumerate(points):
        events.append((x, 'point', i))

    events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else (1 if x[1] == 'point' else 2)))

    count = 0
    results = [0] * len(points)

    for event in events:
        if event[1] == 'start':
            count += 1
        elif event[1] == 'end':
            count -= 1
        elif event[1] == 'point':
            index = event[2]
            results[index] = count

    return results

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    with open(input_file_path, 'r') as f:
        s, p = map(int, f.readline().strip().split())
        segments = [tuple(map(int, f.readline().strip().split())) for _ in range(s)]
        points = list(map(int, f.readline().strip().split()))

    results = count_segments_containing_points(segments, points)

    with open(output_file_path, 'w') as f:
        f.write(' '.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()