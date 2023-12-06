import re

Grid = list[list[int]]


def read_input() -> str:
    with open("input.txt") as f:
        return f.read()


def parse_grid(grid: str) -> Grid:
    lines = grid.splitlines()
    return [[int(val) for val in re.findall(r"\d+", line)] for line in lines[1:]]


def parse_input(full_input: str) -> tuple[list[int], list[Grid]]:
    splits = full_input.split("\n\n")
    seeds = [int(seed) for seed in re.findall(r"\d+", splits[0])]
    grids = [parse_grid(grid) for grid in splits[1:]]
    return seeds, grids


def part1(full_input: str) -> int:
    seeds, grids = parse_input(full_input)
    result = []
    for seed in seeds:
        for grid in grids:
            for row in grid:
                if seed in range(row[1], row[1] + row[2]):
                    seed = row[0] + seed - row[1]
                    break

        result.append(seed)

    return min(result)


def part2(full_input: str) -> int:
    seeds, grids = parse_input(full_input)
    seed_pairs = [
        (start, start + length) for start, length in zip(seeds[::2], seeds[1::2])
    ]
    for grid in grids:
        ranges = []
        for seed_start, seed_end in seed_pairs:
            for row in grid:
                if seed_end <= row[1] or row[1] + row[2] <= seed_start:
                    continue

                intersection_start = max(seed_start, row[1])
                intersection_end = min(seed_end, row[1] + row[2])

                offset = row[0] - row[1]
                ranges.append((intersection_start + offset, intersection_end + offset))

                if seed_start < intersection_start:
                    seed_pairs.append((seed_start, intersection_start))

                if intersection_end < seed_end:
                    seed_pairs.append((intersection_end, seed_end))

                break
            else:
                ranges.append((seed_start, seed_end))

        seed_pairs = ranges

    return min(pair[0] for pair in seed_pairs)


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
