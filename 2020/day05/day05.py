def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one(input):
    max_product = 0
    for line in input:
        row_hint = line[:7]
        column_hint = line[-3:]
        product = 0
        min = 0
        max = 127
        for char in row_hint:
            row = 0
            if char == "F":  # lower half
                max = min + int((max - min) / 2)
            else:  # upper half
                min = max - int((max - min) / 2)
        if max != min:
            raise Exception("!!!!!!!!!")
        else:
            product = min * 8
            min = 0
            max = 7
            for char in column_hint:
                if char == "L":  # lower half
                    max = min + int((max - min) / 2)
                else:  # upper half
                    min = max - int((max - min) / 2)
            product += min
            if product > max_product:
                max_product = product

    return max_product


def part_two(input):
    max_product = 0
    boarding_passes = {}
    for line in input:
        row_hint = line[:7]
        column_hint = line[-3:]
        product = 0
        min = 0
        max = 127
        for char in row_hint:
            row = 0
            if char == "F":  # lower half
                max = min + int((max - min) / 2)
            else:  # upper half
                min = max - int((max - min) / 2)
        if max != min:
            raise Exception("!!!!!!!!!")
        else:
            if not boarding_passes.get(min):
                boarding_passes[min] = []

            product = min * 8
            min = 0
            max = 7
            for char in column_hint:
                if char == "L":  # lower half
                    max = min + int((max - min) / 2)
                else:  # upper half
                    min = max - int((max - min) / 2)
            boarding_passes[product / 8].append(min)
            product += min
            if product > max_product:
                max_product = product
    for index, row in enumerate(sorted(boarding_passes)):
        if len(boarding_passes[row]) < 8 and index != 0:
            missing_seat = None
            for seat in range(7):
                if seat not in boarding_passes[row]:
                    missing_seat = seat
                    break
            return (row * 8) + missing_seat


print(part_one(get_input_lines_from_file()))
print(part_two(get_input_lines_from_file()))
