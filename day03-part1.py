"""
Advent of Code
--- Day 3: Rucksack Reorganization ---
source: https://adventofcode.com/2022/day/3
"""
import string

INPUT_DATA_URL = "https://adventofcode.com/2022/day/3/input"


def get_input_lines():
    with open("data/day03.txt", "r") as file:
        for line in file.readlines():
            yield line.strip()


def common_type_value(badge):
    return string.ascii_letters.index(badge) + 1


def get_sum_of_priorities():
    priorities = []
    for rucksack in get_input_lines():
        mid = len(rucksack) // 2
        common_type = set(rucksack[:mid]) & set(rucksack[mid:])
        priorities.append(common_type_value(common_type.pop()))
    return sum(priorities)


if __name__ == "__main__":
    print(f"sum_of_priorities: {get_sum_of_priorities()}")
