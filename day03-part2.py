"""
Advent of Code
--- Day 3: Rucksack Reorganization ---
source: https://adventofcode.com/2022/day/3
"""
import string
from itertools import islice

INPUT_DATA_URL = "https://adventofcode.com/2022/day/3/input"


def get_input_group():
    with open("data/day03.txt", "r") as file:
        while True:
            lines = list(islice(file, 3))
            if not lines:
                break
            yield lines


def common_type_value(badge):
    return string.ascii_letters.index(badge) + 1


def get_sum_of_priorities():
    priorities = []
    for rucksack in get_input_group():
        s1, s2, s3 = [r.strip() for r in rucksack]
        common_type = set(s1) & set(s2) & set(s3)
        priorities.append(common_type_value(common_type.pop()))

    return sum(priorities)


if __name__ == "__main__":
    print(f"sum_of_priorities: {get_sum_of_priorities()}")
