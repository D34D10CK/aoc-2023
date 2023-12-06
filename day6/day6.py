import re
from math import sqrt


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input1(lines: list[str]) -> list[tuple[int, int]]:
    times = [int(time) for time in re.findall(r"\d+", lines[0])]
    distances = [int(distance) for distance in re.findall(r"\d+", lines[1])]
    return list(zip(times, distances))


def parse_input2(lines: list[str]) -> tuple[int, int]:
    time = int(re.findall(r"\d+", lines[0].replace(" ", ""))[0])
    distance = int(re.findall(r"\d+", lines[1].replace(" ", ""))[0])
    return time, distance


def conmpute_num_ways_to_beat(time: int, distance: int) -> int:
    root_term = sqrt(time**2 - 4 * distance)
    min_time = 0.5 * (time - root_term)
    max_time = 0.5 * (root_term + time)
    return int(max_time) - int(min_time)


def part1(lines: list[str]) -> int:
    result = 1
    for time, distance in parse_input1(lines):
        result *= conmpute_num_ways_to_beat(time, distance)

    return result


def part2(lines: list[str]) -> int:
    time, distance = parse_input2(lines)
    return conmpute_num_ways_to_beat(time, distance)


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
