from collections import Counter

CARD_VALUES_1 = dict(zip("23456789TJQKA", "0123456789ABC"))
CARD_VALUES_2 = dict(zip("J23456789TQKA", "0123456789ABC"))


def read_input() -> list[str]:
    with open("input.txt") as f:
        return f.readlines()


def parse_input(lines: list[str]) -> dict[str, int]:
    return {hand: int(value) for hand, value in (line.split() for line in lines)}


def hand_strength(hand: str, part2: bool = False) -> int:
    card_counts = dict(Counter(hand).most_common())
    counts = list(card_counts.values())
    secondary_score = int(
        "".join(CARD_VALUES_2[card] if part2 else CARD_VALUES_1[card] for card in hand),
        len(CARD_VALUES_1),
    )

    if part2:
        if (jockers := card_counts.pop("J", 0)) in range(1, 5):
            counts = list(card_counts.values())
            counts[0] += jockers

    if counts[0] == 5:
        score = 70000000
    elif counts[0] == 4:
        score = 60000000
    elif len(counts) == 2:
        score = 50000000
    elif counts[0] == 3:
        score = 40000000
    elif counts[0] == 2 and counts[1] == 2:
        score = 30000000
    elif counts[0] == 2:
        score = 20000000
    else:
        score = 10000000

    return score + secondary_score


def part1_and_2(lines: list[str]) -> tuple[int, int]:
    hands = parse_input(lines)
    sorted_hands = dict(sorted(hands.items(), key=lambda hand: hand_strength(hand[0])))
    total1 = 0
    for i, value in enumerate(sorted_hands.values(), start=1):
        total1 += value * i

    sorted_hands = dict(
        sorted(hands.items(), key=lambda hand: hand_strength(hand[0], True))
    )
    total2 = 0
    for i, value in enumerate(sorted_hands.values(), start=1):
        total2 += value * i

    return total1, total2


solution1, solution2 = part1_and_2(read_input())
print("Part 1:", solution1)
print("Part 2:", solution2)
