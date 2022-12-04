"""
Advent of Code
--- Day 4: Camp Cleanup ---
source: https://adventofcode.com/2022/day/4
"""
from itertools import islice

INPUT_DATA_URL = "https://adventofcode.com/2022/day/4/input"


def get_input_pairs():
    with open("data/day04.txt", "r") as file:
        while True:
            lines = list(islice(file, 1))
            if not lines:
                break
            yield lines[0]


def is_contained(pair1, pair2, *args):
    pair11, pair12 = pair1.split("-")
    pair21, pair22 = pair2.split("-")
    contain1 = int(pair11) <= int(pair21) and int(pair12) >= int(pair22)
    contain2 = int(pair21) <= int(pair11) and int(pair22) >= int(pair12)
    result = contain1 or contain2
    return result


def is_overlap(pair1, pair2, *args):
    pair11, pair12 = pair1.split("-")
    pair21, pair22 = pair2.split("-")
    section1 = [x for x in range(int(pair11), int(pair12) + 1)]
    section2 = [x for x in range(int(pair21), int(pair22) + 1)]
    result = set(section1) & set(section2)
    return result


def get_contained_qty():
    contained_qty = 0
    for pairs in get_input_pairs():
        if is_contained(*pairs.strip().split(",")):
            contained_qty += 1
    return contained_qty


def get_overlap_qty():
    overlap_qty = 0
    for pairs in get_input_pairs():
        if is_overlap(*pairs.strip().split(",")):
            overlap_qty += 1
    return overlap_qty


if __name__ == "__main__":
    # print(f"get_contained_qty(): {get_contained_qty()}")  # part1
    print(f"get_overlap_qty(): {get_overlap_qty()}")  # part2
