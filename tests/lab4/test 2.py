import unittest
from io import StringIO
import sys
from collections import defaultdict

def parse_input(age_input, respondent_input):
    boundaries = list(map(int, age_input.split()))
    boundaries.sort()

    respondents = []
    for line in respondent_input.strip().split("\n"):
        if line == "END":
            break
        try:
            name, age = line.rsplit(",", 1)
            respondents.append((name.strip(), int(age.strip())))
        except ValueError:
            raise ValueError(f"Invalid input format: {line}")

    return boundaries, respondents

def group_respondents(boundaries, respondents):
    boundaries = [0] + boundaries + [123]
    groups = defaultdict(list)
    group_names = []

    for i in range(len(boundaries) - 1):
        lower = boundaries[i]
        upper = boundaries[i + 1] - 1
        if upper == 122:
            group_name = "100+"
        else:
            group_name = f"{lower}-{upper}" if upper < 123 else f"{lower}+"
        group_names.append((lower, upper, group_name))

    for name, age in respondents:
        for lower, upper, group_name in group_names:
            if lower <= age <= upper:
                groups[group_name].append((name, age))
                break

    sorted_groups = {}
    for group_name, people in groups.items():
        sorted_groups[group_name] = sorted(people, key=lambda x: (-x[1], x[0]))

    return sorted(sorted_groups.items(),
                  key=lambda x: -boundaries[group_names.index(next(g for g in group_names if g[2] == x[0]))])

def format_output(sorted_groups):
    output = []
    for group_name, people in sorted_groups:
        if people:
            people_str = ", ".join(f"{name} ({age})" for name, age in people)
            output.append(f"{group_name}: {people_str}")
    return output

class TestAgeGroupModule(unittest.TestCase):

    def test_parse_input(self):
        age_input = "18 25 35 45 60 80 100"
        respondent_input = "Кошельков Захар Брониславович, 105\nДьячков Нисон Иринеевич, 88\nEND"
        expected_boundaries = [18, 25, 35, 45, 60, 80, 100]
        expected_respondents = [
            ("Кошельков Захар Брониславович", 105),
            ("Дьячков Нисон Иринеевич", 88)
        ]
        boundaries, respondents = parse_input(age_input, respondent_input)
        self.assertEqual(boundaries, expected_boundaries)
        self.assertEqual(respondents, expected_respondents)

    def test_group_respondents(self):
        boundaries = [18, 25, 35, 45, 60, 80, 100]
        respondents = [
            ("Кошельков Захар Брониславович", 105),
            ("Дьячков Нисон Иринеевич", 88),
            ("Иванов Варлам Якунович", 88),
            ("Старостин Ростислав Ермолаевич", 50),
            ("Ярилова Розалия Трофимовна", 29),
            ("Соколов Андрей Сергеевич", 15),
            ("Егоров Алан Петрович", 7)
        ]
        expected_groups = [
            ("100+", [("Кошельков Захар Брониславович", 105)]),
            ("80-99", [("Дьячков Нисон Иринеевич", 88), ("Иванов Варлам Якунович", 88)]),
            ("45-59", [("Старостин Ростислав Ермолаевич", 50)]),
            ("25-34", [("Ярилова Розалия Трофимовна", 29)]),
            ("0-17", [("Соколов Андрей Сергеевич", 15), ("Егоров Алан Петрович", 7)])
        ]
        grouped = group_respondents(boundaries, respondents)
        self.assertEqual(grouped, expected_groups)

    def test_format_output(self):
        sorted_groups = [
            ("100+", [("Кошельков Захар Брониславович", 105)]),
            ("80-99", [("Дьячков Нисон Иринеевич", 88), ("Иванов Варлам Якунович", 88)]),
            ("45-59", [("Старостин Ростислав Ермолаевич", 50)]),
            ("25-34", [("Ярилова Розалия Трофимовна", 29)]),
            ("0-17", [("Соколов Андрей Сергеевич", 15), ("Егоров Алан Петрович", 7)])
        ]
        expected_output = [
            "100+: Кошельков Захар Брониславович (105)",
            "80-99: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)",
            "45-59: Старостин Ростислав Ермолаевич (50)",
            "25-34: Ярилова Розалия Трофимовна (29)",
            "0-17: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)"
        ]
        output = format_output(sorted_groups)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()