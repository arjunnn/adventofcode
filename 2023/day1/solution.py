import re


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one():
    value_total = 0
    for line in get_input_lines_from_file():
        matches = re.findall(r"\d", line)
        value = int(f"{matches[0]}{matches[-1]}")
        value_total += value
    return value_total

def part_two():
    value_total = 0
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_map = {}
    for index, number in enumerate(numbers):
        number_map[number] = str(index + 1)
    pattern = re.compile(rf"(?=(\d|{'|'.join(numbers)}))")
    for line in get_input_lines_from_file():
        matches = pattern.findall(line)
        value = int(''.join([number_map[number] if len(number) > 1 else number for number in
                             [matches[0], matches[-1]]]))
        # print(f"{line} -> {matches} -> {[matches[0], matches[-1]]} -> {value}")
        value_total += value
    return value_total


if __name__ == "__main__":
    print(part_one())
    print(part_two())