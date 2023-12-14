import numpy as np


def read_input() -> str:
    with open("input.txt") as f:
        return f.read()


def parse_input(full_input: str) -> list[np.ndarray]:
    return [
        np.array([list(l) for l in grid.splitlines()])
        for grid in full_input.split("\n\n")
    ]


def find_symmetry(grid: np.ndarray, black_list: tuple[int, int]) -> tuple[int, int]:
    rows, cols = grid.shape

    for i in range(1, cols):
        if np.array_equal(
            grid[:, i - min(i, cols - i) : i],
            grid[:, i : i + min(i, cols - i)][:, ::-1],
        ):
            if (0, i) != black_list:
                return (0, i)

    for i in range(1, rows):
        if np.array_equal(
            grid[i - min(i, rows - i) : i, :], grid[i : i + min(i, rows - i), :][::-1]
        ):
            if (i, 0) != black_list:
                return (i, 0)

    return (0, 0)


def part1(full_input: str) -> int:
    total = 0
    for grid in parse_input(full_input):
        horizontal, vertical = find_symmetry(grid, (0, 0))
        total += vertical + 100 * horizontal

    return total


def part2(full_input: str) -> int:
    total = 0
    for grid in parse_input(full_input):
        symmetry = find_symmetry(grid, (0, 0))
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                original_grid = grid.copy()
                if grid[i, j] == "#":
                    grid[i, j] = "."
                else:
                    grid[i, j] = "#"

                horizontal, vertical = find_symmetry(grid, symmetry)
                total += vertical + 100 * horizontal
                grid = original_grid
                if horizontal != 0 or vertical != 0:
                    break
            else:
                continue
            break

    return total


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
