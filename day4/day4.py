import re


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input(lines: list[str]):
    for line in lines:
        card_start = line.index(":")
        card, winning_numbers = line[card_start:].split("|")
        card = re.findall(r"\d+", card)
        winning_numbers = re.findall(r"\d+", winning_numbers)
        yield set(card) & set(winning_numbers)


def part1(lines: list[str]) -> int:
    total = 0
    for hits in parse_input(lines):
        if hits:
            total += 2 ** (len(hits) - 1)

    return total


def part2(lines: list[str]) -> int:
    number_of_wins = [len(card) for card in parse_input(lines)]
    cards = [1] * len(number_of_wins)
    for card_idx, number_of_cards in enumerate(cards):
        for i in range(card_idx + 1, card_idx + 1 + number_of_wins[card_idx]):
            cards[i] += number_of_cards

    return sum(cards)


print("Part 1:", part1(read_input()))
print("Part 2:", part2(read_input()))
