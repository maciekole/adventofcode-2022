"""
Advent of Code
--- Day 2: Rock, Paper, Scissors ---
source: https://adventofcode.com/2022/day/2

Rock [+1]: A / X
Paper [+2]: B / Y
Scissors [+3]: C / Z

Points: lose-0, draw-3, win-6
"""
INPUT_DATA_URL = "https://adventofcode.com/2022/day/2/input"
SHAPES = {"X": 1, "Y": 2, "Z": 3, "A": "X", "B": "Y", "C": "Z"}
POINTS = {"lose": 0, "draw": 3, "win": 6}


def win_draw_lose(figure1, figure2):
    # draw
    if SHAPES[figure1] == figure2:
        return POINTS["draw"]

    if figure1 == "A":
        return POINTS["win"] if figure2 == "Y" else POINTS["lose"]

    if figure1 == "B":
        return POINTS["win"] if figure2 == "Z" else POINTS["lose"]

    if figure1 == "C":
        return POINTS["win"] if figure2 == "X" else POINTS["lose"]


def check_round_result(opponent_shape, my_shape, *args):
    result = 0
    # win/draw/lose
    result += win_draw_lose(opponent_shape, my_shape)

    # shape value
    result += SHAPES.get(my_shape, 0)
    return result


def get_round_result():
    with open("data/day02.txt", "r") as file:
        for line in file.readlines():
            yield check_round_result(*line.strip().split(" "))


if __name__ == "__main__":
    print(f"part1: {sum(get_round_result())}")
