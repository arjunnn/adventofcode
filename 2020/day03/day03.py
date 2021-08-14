import sys
import os
import re
import math


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


if __name__ == "__main__":
    input = get_input_lines_from_file()
    right = 3
    down = 1

    def part_one(input=input, down=down, right=right):
        next_index = 0
        tree_count = 0
        skip = 1
        pointer = ""
        for row in input:
            if skip > 1:
                skip -= 1
                continue
            chars = [char for char in row]
            pointer = chars[next_index]
            if pointer == "#":
                tree_count += 1
            for pos in range(right):
                try:
                    next_index += 1
                    pointer = chars[next_index]
                except IndexError:
                    next_index = 0
                    pointer = chars[next_index]
            skip = down
        return tree_count

    def part_two(input=input):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        tree_product = 1
        for slope in slopes:
            [right, down] = slope
            tree_count = part_one(down=down, right=right)
            tree_product = tree_product * tree_count
        return tree_product

    print(part_one(input=input, down=down, right=right))
    print(part_two())
