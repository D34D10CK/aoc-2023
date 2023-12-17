import numpy as np


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def throw_beam(
    grid: list[str],
    start: tuple[int, int],
    direction: str,
    directions: list[list[list[str]]],
    energized: np.ndarray,
) -> np.ndarray:
    stack = [(start, direction)]

    while stack:
        (x, y), direction = stack.pop()

        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            continue

        if direction in directions[x][y]:
            continue

        directions[x][y].append(direction)
        energized[x, y] = True

        if direction == "u":
            if grid[x][y] in [".", "|"]:
                stack.append(((x - 1, y), "u"))
            elif grid[x][y] == "/":
                stack.append(((x, y + 1), "r"))
            elif grid[x][y] == "\\":
                stack.append(((x, y - 1), "l"))
            elif grid[x][y] == "-":
                stack.append(((x, y - 1), "l"))
                stack.append(((x, y + 1), "r"))

        elif direction == "d":
            if grid[x][y] in [".", "|"]:
                stack.append(((x + 1, y), "d"))
            elif grid[x][y] == "/":
                stack.append(((x, y - 1), "l"))
            elif grid[x][y] == "\\":
                stack.append(((x, y + 1), "r"))
            elif grid[x][y] == "-":
                stack.append(((x, y - 1), "l"))
                stack.append(((x, y + 1), "r"))

        elif direction == "l":
            if grid[x][y] in [".", "-"]:
                stack.append(((x, y - 1), "l"))
            elif grid[x][y] == "/":
                stack.append(((x + 1, y), "d"))
            elif grid[x][y] == "\\":
                stack.append(((x - 1, y), "u"))
            elif grid[x][y] == "|":
                stack.append(((x - 1, y), "u"))
                stack.append(((x + 1, y), "d"))

        elif direction == "r":
            if grid[x][y] in [".", "-"]:
                stack.append(((x, y + 1), "r"))
            elif grid[x][y] == "/":
                stack.append(((x - 1, y), "u"))
            elif grid[x][y] == "\\":
                stack.append(((x + 1, y), "d"))
            elif grid[x][y] == "|":
                stack.append(((x - 1, y), "u"))
                stack.append(((x + 1, y), "d"))

    return energized


def part1(lines: list[str]) -> int:
    directions = [[[] for _ in range(len(lines[0]))] for _ in lines]
    energized_init = np.zeros((len(lines), len(lines[0])), dtype=bool)
    energized = throw_beam(lines, (0, 0), "r", directions, energized_init)
    return energized.sum()


def part2(lines: list[str]) -> int:
    top = list(zip([0] * len(lines[0]), range(len(lines[0])), ["d"] * len(lines[0])))
    bottom = list(
        zip(
            [len(lines) - 1] * len(lines[0]),
            range(len(lines[0])),
            ["u"] * len(lines[0]),
        )
    )
    left = list(zip(range(len(lines)), [0] * len(lines), ["r"] * len(lines)))
    right = list(
        zip(range(len(lines)), [len(lines[0]) - 1] * len(lines), ["l"] * len(lines))
    )

    ret = 0
    for x, y, direction in top + bottom + left + right:
        directions = [[[] for _ in range(len(lines[0]))] for _ in lines]
        energized_init = np.zeros((len(lines), len(lines[0])), dtype=bool)
        energized = throw_beam(lines, (x, y), direction, directions, energized_init)
        ret = max(ret, energized.sum())

    return ret


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
