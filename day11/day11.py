from itertools import combinations

import numpy as np


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def count_empty_columns_before(grid: np.ndarray, y: int) -> int:
    return sum(np.all(grid[:, i] == ".") for i in range(y))


def count_empty_rows_before(grid: np.ndarray, x: int) -> int:
    return sum(np.all(grid[i] == ".") for i in range(x))


def get_expanded_galaxies(lines: list[str], amount: int) -> list[tuple[int, int]]:
    amount = amount - 1
    grid = np.array([list(line) for line in lines])
    galaxies = get_galaxies(grid)
    for i, (x, y) in enumerate(galaxies):
        galaxies[i] = (
            x + count_empty_rows_before(grid, x) * amount,
            y + count_empty_columns_before(grid, y) * amount,
        )

    return galaxies


def get_galaxies(grid: np.ndarray) -> list[tuple[int, int]]:
    return list(zip(*np.where(grid == "#")))


def compute_sum_of_shortest_paths(galaxies: list[tuple[int, int]]) -> int:
    pairs = list(combinations(galaxies, 2))
    total = 0
    for pair in pairs:
        total += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

    return total


def part1(lines: list[str]) -> int:
    galaxies = get_expanded_galaxies(lines, 2)
    return compute_sum_of_shortest_paths(galaxies)


def part2(lines: list[str]) -> int:
    galaxies = get_expanded_galaxies(lines, 1000000)
    return compute_sum_of_shortest_paths(galaxies)


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
