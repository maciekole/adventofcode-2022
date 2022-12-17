"""
Advent of Code
--- Day 6: Tuning Trouble ---
source: https://adventofcode.com/2022/day/6
"""
from collections import deque

INPUT_DATA_URL = "https://adventofcode.com/2022/day/6/input"
PACKET_SIZE = 4  # pt.1
MESSAGE_SIZE = 14  # pt2


class MarkerException(Exception):
    pass


def marker_found_handling():
    print("--> coroutine started")
    while True:
        try:
            yield from get_datastream()
        except MarkerException:
            print("--> coroutine stopped")
            break


def get_datastream():
    counter = 0
    with open("data/day06.txt", "r") as file:
        for stream_bit in file.read():
            counter += 1
            print(f"--> {counter}")
            yield stream_bit


def main():
    marker_frame = deque(MESSAGE_SIZE * [], MESSAGE_SIZE)
    datastream_coro = marker_found_handling()
    for character in datastream_coro:
        marker_frame.append(character)
        if len(set(marker_frame)) < MESSAGE_SIZE and None not in set(
            marker_frame
        ):
            continue
        else:
            datastream_coro.throw(MarkerException)

    return sorted(marker_frame)


if __name__ == "__main__":
    main()
