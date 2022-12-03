"""
Advent of Code
--- Day 2: Rock, Paper, Scissors ---
source: https://adventofcode.com/2022/day/2

Rock [+1]: A / X
Paper [+2]: B / Y
Scissors [+3]: C / Z

Points: lose [X]-0, draw [Y]-3, win [Z]-6
"""
INPUT_DATA_URL = "https://adventofcode.com/2022/day/2/input"
SHAPES = {"A": 1, "B": 2, "C": 3}
WIN = {"A": "B", "B": "C", "C": "A"}
LOSE = {"A": "C", "B": "A", "C": "B"}
POINTS = {"lose": 0, "draw": 3, "win": 6}


def check_round_result(opponent_shape, my_result, *args):
    result = 0
    my_shape = False
    # draw
    if my_result == "Y":
        result += POINTS["draw"]
        my_shape = opponent_shape

    # win
    if my_result == "Z":
        result += POINTS["win"]
        my_shape = WIN.get(opponent_shape, False)

    # lose
    if my_result == "X":
        result += POINTS["lose"]
        my_shape = LOSE.get(opponent_shape, False)

    result += SHAPES.get(my_shape, 0)
    return result


def get_round_result():
    with open("data/day02.txt", "r") as file:
        for line in file.readlines():
            yield check_round_result(*line.strip().split(" "))


if __name__ == "__main__":
    print(f"part2: {sum(get_round_result())}")
