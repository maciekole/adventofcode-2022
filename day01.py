"""
Advnt of Code
--- Day 1: Calorie Counting ---
source: https://adventofcode.com/2022/day/1
"""
INPUT_DATA_URL = "https://adventofcode.com/2022/day/1/input"

def get_elfs_calories():
    calories = 0
    with open('data/day01.txt', 'r') as file:
        for line in file.readlines():
            if line == '\n':
                yield calories
                calories = 0
                continue
            calories += int(line)
            

def main():
    result = []
    for elf in get_elfs_calories():
        result.append(elf)
    return sorted(result)

if __name__ == '__main__':
    max_calories = main()
    print(f"max value: {max_calories[-1]}")
    print(f"sum of highest 3: {sum(max_calories[-3:])}")
