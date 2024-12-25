import os

def process_packets(buffer_size, packets):
    finish_time = []
    results = []
    current_time = 0

    for arrival_time, process_time in packets:
        while finish_time and finish_time[0] <= arrival_time:
            finish_time.pop(0)

        if len(finish_time) < buffer_size:
            if not finish_time:
                start_time = arrival_time
            else:
                start_time = finish_time[-1]

            finish_time.append(start_time + process_time)
            results.append(start_time)
        else:
            results.append(-1)

    return results

def main():
    input_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'txtf', 'input.txt'))
    output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'txtf', 'output.txt'))

    with open(input_file_path, 'r') as f:
        buffer_size, n = map(int, f.readline().strip().split())
        packets = [tuple(map(int, f.readline().strip().split())) for _ in range(n)]

    results = process_packets(buffer_size, packets)

    with open(output_file_path, 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == '__main__':
    main()
