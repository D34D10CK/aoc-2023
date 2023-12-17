def read_input() -> str:
    with open("input.txt") as f:
        return f.read()


def parse_input(full_input: str) -> list[str]:
    return [line.strip() for line in full_input.split(",")]


def hash_str(word: str) -> int:
    current_value = 0
    for char in word:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


def part1(full_input: str) -> int:
    return sum(hash_str(word) for word in parse_input(full_input))


def part2(full_input: str) -> int:
    boxes = [{} for _ in range(256)]
    for word in parse_input(full_input):
        if "=" in word:
            lens, focal = word.split("=")
            box = hash_str(lens)
            boxes[box][lens] = focal
        else:
            lens = word[:-1]
            box = hash_str(lens)
            if lens in boxes[box]:
                del boxes[box][lens]

    total = 0
    for i, box in enumerate(boxes):
        if box:
            total += (i + 1) * sum(
                int(focal) * (j + 1) for j, focal in enumerate(box.values())
            )

    return total


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
