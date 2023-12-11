from itertools import product

import numpy as np
from shapely.geometry import Point, Polygon


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def get_loop(lines: list[str]) -> list[tuple[int, int]]:
    grid = np.array([list(line.strip()) for line in lines])
    x, y = np.where(grid == "S")
    x = x[0]
    y = y[0]
    previous_x = -1
    previous_y = -1

    loop = []
    while True:
        current_pipe = grid[x, y]
        x_copy = x
        y_copy = y
        match current_pipe:
            case "S":
                if previous_y != -1 and previous_x != -1:
                    return loop

                if grid[x + 1, y] in "|JL":
                    x = x + 1
                elif grid[x - 1, y] in "|F7":
                    x = x - 1
                elif grid[x, y + 1] in "-J7":
                    y = y + 1
                else:
                    y = y - 1

            case "|":
                if previous_x < x:
                    x = x + 1
                else:
                    x = x - 1
            case "-":
                if previous_y < y:
                    y = y + 1
                else:
                    y = y - 1
            case "L":
                if previous_y == y:
                    y = y + 1
                else:
                    x = x - 1
            case "J":
                if previous_y == y:
                    y = y - 1
                else:
                    x = x - 1
            case "7":
                if previous_x == x:
                    x = x + 1
                else:
                    y = y - 1
            case "F":
                if previous_x == x:
                    x = x + 1
                else:
                    y = y + 1

        previous_x = x_copy
        previous_y = y_copy
        loop.append((x, y))


def part1(lines: list[str]) -> int:
    return len(get_loop(lines)) // 2


def part2(lines: list[str]) -> int:
    loop = get_loop(lines)
    polygon = Polygon(loop)
    grid = set(product(range(0, len(lines)), range(0, len(lines[0])))) - set(loop)
    inside_points = [point for point in grid if Point(point).within(polygon)]
    return len(inside_points)


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
