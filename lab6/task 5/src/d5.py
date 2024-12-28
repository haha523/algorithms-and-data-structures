import os
from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        votes = f.readlines()
    return votes

def write_output(file_path, results):
    with open(file_path, 'w') as f:
        for candidate, total_votes in results:
            f.write(f"{candidate} {total_votes}\n")

def main():
    input_path = os.path.join('..', 'txtf', 'input.txt')
    output_path = os.path.join('..', 'txtf', 'output.txt')

    votes = read_input(input_path)
    vote_count = defaultdict(int)

    for vote in votes:
        parts = vote.split()
        candidate = parts[0]
        count = int(parts[1])  
        vote_count[candidate] += count

    sorted_results = sorted(vote_count.items())

    write_output(output_path, sorted_results)

if __name__ == "__main__":
    main()
