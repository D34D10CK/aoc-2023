import re


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def read_input():
    with open("input.txt") as f:
        return f.readlines()


def part1(lines):
    total = 0
    for line in lines:
        numbers = re.findall(r"\d", line)
        total += int(numbers[0] + numbers[-1])

    return total


def part2(lines):
    total = 0
    for line in lines:
        numbers = re.findall(rf"(?=({'|'.join(DIGITS.keys())}|\d))", line)
        calibration_value = int(
            DIGITS.get(numbers[0], numbers[0]) + DIGITS.get(numbers[-1], numbers[-1])
        )
        total += calibration_value

    return total


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
