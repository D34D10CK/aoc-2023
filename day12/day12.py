from functools import cache


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.read().splitlines()


def count_valid(input_string: str, group_sizes: list[int]) -> int:
    @cache
    def count_valid_(input_idx: int, group_idx: int, used: int) -> int:
        if input_idx == len(input_string):
            if group_idx == len(group_sizes) and used == 0:
                return 1

            if group_idx == len(group_sizes) - 1 and used == group_sizes[group_idx]:
                return 1

            return 0

        ret = 0
        if input_string[input_idx] in ["#", "?"]:
            if group_idx < len(group_sizes) and used < group_sizes[group_idx]:
                ret += count_valid_(input_idx + 1, group_idx, used + 1)

        if input_string[input_idx] in [".", "?"]:
            if group_idx < len(group_sizes) and used == group_sizes[group_idx]:
                ret += count_valid_(input_idx + 1, group_idx + 1, 0)
            elif used == 0:
                ret += count_valid_(input_idx + 1, group_idx, 0)

        return ret

    return count_valid_(0, 0, 0)


def parse_input(lines: list[str]) -> list[tuple[str, list[int]]]:
    return [
        (chars, [int(num) for num in nums.split(",")])
        for chars, nums in (line.split() for line in lines)
    ]


def part1(lines: list[str]) -> int:
    return sum(count_valid(line, groups) for line, groups in parse_input(lines))


def part2(lines: list[str]) -> int:
    total = 0
    for line, groups in parse_input(lines):
        line = ((line + "?") * 5)[:-1]
        groups = groups * 5
        total += count_valid(line, groups)

    return total


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
