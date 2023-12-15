import numpy as np


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def parse_input(lines: list[str]) -> np.ndarray:
    return np.array([list(l) for l in lines])


def move_north(grid: np.ndarray) -> np.ndarray:
    circles = np.argwhere(grid == "O")
    for x, y in circles:
        blocks = np.argwhere(grid != ".")
        block = blocks[(blocks[:, 0] < x) & (blocks[:, 1] == y)]
        if len(block) > 0:
            block = block[-1]
            grid[block[0] + 1, block[1]] = "O"
            if x != block[0] + 1:
                grid[x, y] = "."
        else:
            if x != 0:
                grid[0, y] = "O"
                grid[x, y] = "."

    return grid


def part1(lines: list[str]) -> int:
    grid = move_north(parse_input(lines))
    return sum(len(grid) - np.argwhere(grid == "O")[:, 0])


def part2(lines: list[str]) -> int:
    grid = parse_input(lines)
    history = [grid.tolist()]
    while True:
        for _ in range(4):
            grid = move_north(grid)
            grid = np.rot90(grid, k=3)

        grid_list = grid.tolist()
        if grid_list in history:
            period_start = history.index(grid_list)
            period_length = len(history) - period_start
            break

        history.append(grid_list)

    grid = history[(1000000000 - period_start) % period_length + period_start]
    return sum(len(grid) - np.argwhere(np.array(grid) == "O")[:, 0])


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
