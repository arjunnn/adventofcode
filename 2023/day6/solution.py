def get_input_lines_from_file():
    with open("sample", "r") as input_file:
        return input_file.read().splitlines()


def get_distance_for_hold(hold: int):
    pass


def part_one() -> int:
    lines = get_input_lines_from_file()
    times = [int(val) for val in filter(lambda x: x, lines[0].split(":")[1].strip().split(" "))]
    distances = [int(val) for val in filter(lambda x: x, lines[1].split(":")[1].strip().split(" "))]
    print(times, distances)
    index = 0
    winning_moves = 1
    while index < len(times):

    return 0


if __name__ == "__main__":
    print(part_one())