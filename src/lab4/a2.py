import sys
from collections import defaultdict

def parse_input():
    """Parses input data and returns age group boundaries and respondent data."""
    # First, parse age group boundaries from command line arguments
    if len(sys.argv) < 2:
        raise ValueError("Please provide age group boundaries as command-line arguments.")

    boundaries = list(map(int, sys.argv[1:]))
    boundaries.sort()

    # Parse respondents from standard input
    respondents = []
    for line in sys.stdin:
        line = line.strip()
        if line == "END":
            break
        try:
            name, age = line.rsplit(",", 1)
            respondents.append((name.strip(), int(age.strip())))
        except ValueError:
            raise ValueError(f"Invalid input format: {line}")

    return boundaries, respondents


def group_respondents(boundaries, respondents):
    """Groups respondents by age groups based on provided boundaries."""
    # Extend boundaries to include groups 0- and 123+
    boundaries = [0] + boundaries + [123]

    # Define groups and group names
    groups = defaultdict(list)
    group_names = []
    for i in range(len(boundaries) - 1):
        lower = boundaries[i]
        upper = boundaries[i + 1] - 1
        if i == len(boundaries) - 2:
            group_name = f"{lower}+"
        else:
            group_name = f"{lower}-{upper}"
        group_names.append((lower, upper, group_name))

    # Assign respondents to groups
    for name, age in respondents:
        for lower, upper, group_name in group_names:
            if lower <= age <= upper:
                groups[group_name].append((name, age))
                break

    # Sort groups and respondents within each group
    sorted_groups = {}
    for group_name, people in groups.items():
        sorted_groups[group_name] = sorted(people, key=lambda x: (-x[1], x[0]))

    return sorted(sorted_groups.items(),
                  key=lambda x: -boundaries[group_names.index(next(g for g in group_names if g[2] == x[0]))])


def format_output(sorted_groups):
    """Formats grouped respondents for output."""
    output = []
    for group_name, people in sorted_groups:
        if people:  # Skip empty groups
            people_str = ", ".join(f"{name} ({age})" for name, age in people)
            output.append(f"{group_name}: {people_str}")
    return output


if __name__ == "__main__":
    try:
        boundaries, respondents = parse_input()
        sorted_groups = group_respondents(boundaries, respondents)
        output = format_output(sorted_groups)
        for line in output:
            print(line)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)