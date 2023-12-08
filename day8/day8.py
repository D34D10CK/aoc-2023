from itertools import cycle
from math import lcm


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input(lines: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    moves = lines[0].strip()
    maps = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}
    return moves, maps


def part1(lines: list[str]) -> int:
    moves, coordinates = parse_input(lines)
    moves = cycle(moves)
    location = "AAA"
    for i, move in enumerate(moves):
        if location == "ZZZ":
            return i

        match (move):
            case "L":
                location = coordinates[location][0]
            case "R":
                location = coordinates[location][1]


def find_cycle_length(
    moves: str, coordinates: dict[str, tuple[str, str]], start: str
) -> int:
    past_locations = [start]
    for i, move in enumerate(cycle(moves)):
        if (
            past_locations[-1].endswith("Z")
            and past_locations[-1] in past_locations[:-1]
        ):
            return i - past_locations.index(past_locations[-1])

        match (move):
            case "L":
                past_locations.append(coordinates[past_locations[-1]][0])
            case "R":
                past_locations.append(coordinates[past_locations[-1]][1])


def part2(lines: list[str]) -> int:
    moves, coordinates = parse_input(lines)
    locations = [
        coordinate for coordinate in coordinates.keys() if coordinate.endswith("A")
    ]
    cycle_lengths = []
    for location in locations:
        cycle_length = find_cycle_length(moves, coordinates, location)
        cycle_lengths.append(cycle_length)

    return lcm(*cycle_lengths)


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
