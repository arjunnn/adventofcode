import re
from functools import reduce


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one():
    boundaries = {"red": 12, "green": 13, "blue": 14}
    possible_games = []
    pattern = re.compile(rf"(\d+) ({'|'.join(boundaries.keys())})")
    games = get_input_lines_from_file()
    for index, game in enumerate(games):
        game_id = index + 1
        sets = game.split(":")[1].strip().split(";")
        sums = dict.fromkeys(boundaries.keys(), 0)
        for _set in sets:
            matches = pattern.findall(_set)
            for match in matches:
                sums[match[1]] = max(sums[match[1]], int(match[0]))
        # print([(colour, sums[colour], sums[colour] <= boundaries[colour]) for colour, total in sums.items()])
        if all([boundaries[colour] >= sums[colour] for colour, total in sums.items()]):
            possible_games.append(game_id)
    return sum(possible_games)


def part_two():
    boundaries = {"red": 12, "green": 13, "blue": 14}
    pattern = re.compile(rf"(\d+) ({'|'.join(boundaries.keys())})")
    games = get_input_lines_from_file()
    sum_of_powers = 0
    for index, game in enumerate(games):
        game_id = index + 1
        sets = game.split(":")[1].strip().split(";")
        sums = dict.fromkeys(boundaries.keys(), 0)
        for _set in sets:
            matches = pattern.findall(_set)
            print(game_id, matches)
            for match in matches:
                sums[match[1]] = max(sums[match[1]], int(match[0]))
        sum_of_powers += reduce((lambda x, y: x * y), sums.values())
    return sum_of_powers


if __name__ == "__main__":
    print(part_one())
    print(part_two())
