from functools import lru_cache


@lru_cache()
def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one() -> int:
    total_score = []
    for line_index, line in enumerate(get_input_lines_from_file()):
        p1, p2 = line.split(' | ')
        winning_numbers = set([num for num in filter(lambda x: x, p1.split(':')[1].strip().split(" "))])
        scratched_numbers = set([num for num in filter(lambda x: x, p2.split(" "))])
        intersection = winning_numbers.intersection(scratched_numbers)
        if intersection:
            if len(intersection) == 1:
                total_score.append(1)
            else:
                total_score.append((2 ** (len(intersection) - 1)))
    return sum(total_score)


@lru_cache()
def get_winning_matches_for_card(line: str, line_index: int) -> int:
    total_cards = 0
    p1, p2 = line.split(' | ')
    winning_numbers = set([num for num in filter(lambda x: x, p1.split(':')[1].strip().split(" "))])
    scratched_numbers = set([num for num in filter(lambda x: x, p2.split(" "))])
    intersection = winning_numbers.intersection(scratched_numbers)
    total_cards += len(intersection)
    if intersection:
        for match in range(line_index + 1, (line_index + 1 + len(intersection))):
            total_cards += get_winning_matches_for_card(get_input_lines_from_file()[match], match)
    return total_cards


def part_two() -> int:
    total_cards = 0
    lines = get_input_lines_from_file()
    for line_index, line in enumerate(lines):
        total_cards += (1 + get_winning_matches_for_card(line, line_index))
    return total_cards


if __name__ == "__main__":
    print(part_one())
    print(part_two())
    print(get_winning_matches_for_card.cache_info())
