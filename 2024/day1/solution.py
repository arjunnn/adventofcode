def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one():
    lines = get_input_lines_from_file()
    left_list, right_list = [], []
    for line in lines:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    distances = []

    for index, left_num in enumerate(left_list):
        distances.append(abs(left_num - right_list[index]))

    return sum(distances)


def part_two():
    lines = get_input_lines_from_file()
    left_list, right_list = [], {}
    for line in lines:
        left, right = line.split("   ")
        left_list.append(int(left))
        if int(right) not in right_list:
            right_list[int(right)] = 0
        right_list[int(right)] += 1

    for left_num in left_list:
        if left_num in right_list:
            right_list[left_num] += 1

    similarity_score = []

    for num, occurances in right_list.items():
        if occurances:
            similarity_score.append(num * (occurances - 1))

    return sum(similarity_score)


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
