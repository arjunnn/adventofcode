def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one(input):
    cleaned_input = []
    group_answers = ""
    for row in input:
        if row:
            group_answers += row
        else:
            cleaned_input.append(group_answers)
            group_answers = ""
    if group_answers:
        cleaned_input.append(group_answers)
    count = 0
    for group in cleaned_input:
        count += len(set([answer for answer in group]))
    return count


def part_two(input):
    answers = []
    answers_count = 0
    previous_row_was_empty = True
    for row in input:
        if row:
            if answers:
                answers = [char for char in row if char in answers]
            else:
                answers = [char for char in row if previous_row_was_empty]
            previous_row_was_empty = False
        else:
            answers_count += len(answers)
            answers = []
            previous_row_was_empty = True
    if answers:
        answers_count += len(answers)
    return answers_count


print(part_one(get_input_lines_from_file()))
print(part_two(get_input_lines_from_file()))
