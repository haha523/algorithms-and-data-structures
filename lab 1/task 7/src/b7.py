import os

def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        savings = list(map(float, file.readline().strip().split()))

        residents = [(savings[i], i + 1) for i in range(n)]

        residents.sort()

    poorest = residents[0][1]
    richest = residents[-1][1]
    median = residents[n // 2][1]

    with open(output_file, 'w') as file:
        file.write(f"{poorest} {median} {richest}\n")


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, '..', 'txtf', 'input.txt')
    output_file_path = os.path.join(current_dir, '..', 'txtf', 'output.txt')

    process_data(input_file_path, output_file_path)


if __name__ == "__main__":
    main()
