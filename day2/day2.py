import re
from math import prod


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def is_possible(color_counts: dict[str, int]) -> bool:
    return (
        color_counts["red"] <= 12
        and color_counts["green"] <= 13
        and color_counts["blue"] <= 14
    )


def part1_and_2(lines: list[str]) -> tuple[int, int]:
    sum_of_game_ids = 0
    total_power = 0
    for game_id, line in enumerate(lines, start=1):
        max_color_counts = dict.fromkeys(["red", "green", "blue"], 0)
        for count, color in re.findall(r"(\d+) (red|green|blue)", line):
            max_color_counts[color] = max(max_color_counts[color], int(count))

        if is_possible(max_color_counts):
            sum_of_game_ids += game_id

        total_power += prod(max_color_counts.values())

    return sum_of_game_ids, total_power


part1, part2 = part1_and_2(read_input())
print("Part 1:", part1)
print("Part 1:", part2)
