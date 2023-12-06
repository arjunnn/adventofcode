import re
from functools import lru_cache
from typing import Union, List

NUMBER_PATTERN = re.compile(r"\d+")
SYMBOL_PATTERN = re.compile(r"[^\d.]")


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


@lru_cache()
def get_chars_from_line(line: str, char_type: str) -> List[tuple[Union[int, str], tuple]]:
    char_map = []
    if char_type == "number":
        numbers = NUMBER_PATTERN.finditer(line)
        for number in numbers:
            value = int(line[number.start(): number.end()])
            char_map.append((value, number.span()))
    elif char_type == "symbol":
        symbols = SYMBOL_PATTERN.finditer(line)
        for symbol in symbols:
            value = line[symbol.start()]
            char_map.append((value, symbol.span()))
    return char_map


def find_numbers_within_boundary(line: str, boundaries) -> List[int]:
    numbers = get_chars_from_line(line, "number")
    adjacent_numbers = []
    for num, num_pos in numbers:
        number_span = {pos for pos in range(num_pos[0], num_pos[1])}
        if boundaries.intersection(number_span):
            adjacent_numbers.append(num)
    return adjacent_numbers


def part_one():
    lines = get_input_lines_from_file()
    part_numbers = []
    for line_index, line in enumerate(lines):
        symbols = get_chars_from_line(line, "symbol")
        for sym, sym_pos in symbols:
            boundaries = {pos for pos in range(max(0, sym_pos[0] - 1), min(sym_pos[1] + 1, len(line) - 1))}
            if line_index > 0:
                part_numbers.extend(find_numbers_within_boundary(lines[line_index - 1], boundaries))
            if line_index + 1 < len(lines):
                part_numbers.extend(find_numbers_within_boundary(lines[line_index + 1], boundaries))
            part_numbers.extend(find_numbers_within_boundary(line, boundaries))
    return sum(part_numbers)


def part_two():
    lines = get_input_lines_from_file()
    gear_ratios = []
    for line_index, line in enumerate(lines):
        symbols = get_chars_from_line(line, "symbol")
        for sym, sym_pos in symbols:
            if sym != "*":
                continue
            boundaries = {pos for pos in range(max(0, sym_pos[0] - 1), min(sym_pos[1] + 1, len(line) - 1))}
            adjacent_numbers = []
            if line_index > 0:
                adjacent_numbers.extend(find_numbers_within_boundary(lines[line_index - 1], boundaries))
            if line_index + 1 < len(lines):
                adjacent_numbers.extend(find_numbers_within_boundary(lines[line_index + 1], boundaries))
            adjacent_numbers.extend(find_numbers_within_boundary(line, boundaries))
            if len(adjacent_numbers) == 2:
                gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])
    return sum(gear_ratios)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
    print(get_chars_from_line.cache_info())
