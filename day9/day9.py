import numpy as np


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input(lines: list[str]) -> list[np.ndarray]:
    return [np.array([int(num) for num in line.split()]) for line in lines]


def forecast_future(line: np.ndarray) -> int:
    if all(line == line[0]):
        return line[0]

    new_line = line[1:] - line[:-1]
    return line[-1] + forecast_future(new_line)


def forecast_past(line: np.ndarray) -> int:
    if all(line == line[0]):
        return line[0]

    new_line = line[1:] - line[:-1]
    return line[0] - forecast_past(new_line)


def part1(lines: list[str]) -> int:
    return sum(forecast_future(line) for line in parse_input(lines))


def part2(lines: list[str]) -> int:
    return sum(forecast_past(line) for line in parse_input(lines))


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
