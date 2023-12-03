import re
from collections import defaultdict
from functools import reduce
from math import prod


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def extract_numbers(lines: list[str]) -> dict[tuple[int, int, int], int]:
    numbers = {}
    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            numbers[(match.start(), match.end(), i)] = int(match[0])

    return numbers


def extract_symbols(lines: list[str]) -> dict[str, set[tuple[int, int]]]:
    symbols = defaultdict(set)
    for i, line in enumerate(lines):
        for match in re.finditer(r"[^\d\n.]", line):
            symbols[match[0]].add((match.start(), i))

    return symbols


def part1(lines: list[str]) -> int:
    numbers = extract_numbers(lines)
    symbols = reduce(set.union, extract_symbols(lines).values())
    total = 0
    for (number_start, number_end, number_y), number in numbers.items():
        for x_symbol, y_symbol in symbols:
            if x_symbol in range(
                number_start - 1, number_end + 1
            ) and y_symbol in range(number_y - 1, number_y + 2):
                total += number

    return total


def part2(lines: list[str]) -> int:
    numbers = extract_numbers(lines)
    gears = extract_symbols(lines)["*"]
    total = 0
    for x_gear, y_gear in gears:
        intersections = []
        for (number_start, number_end, number_y), number in numbers.items():
            if x_gear in range(number_start - 1, number_end + 1) and y_gear in range(
                number_y - 1, number_y + 2
            ):
                intersections.append(number)

        if len(intersections) == 2:
            total += prod(intersections)

    return total


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
