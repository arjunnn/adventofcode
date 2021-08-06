import sys
import os
import re
import math


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


if __name__ == "__main__":
    input = get_input_lines_from_file()

    def part_one(input):
        valid_passwords_count = 0
        for line in input:
            line = line.split(":")
            password_policy = line[0].split(" ")
            char = password_policy[1]
            [min, max] = password_policy[0].split("-")
            password = line[1].strip()
            matches = len(re.findall(char, password))
            if matches >= int(min) and matches <= int(max):
                valid_passwords_count += 1
        print(valid_passwords_count)

    def part_two(input):
        valid_passwords_count = 0
        for line in input:
            line = line.split(":")
            password_policy = line[0].split(" ")
            char = password_policy[1]
            [pos1, pos2] = password_policy[0].split("-")
            password = line[1].strip()
            pos1 = password.find(char, int(pos1) - 1, int(pos1))
            pos2 = password.find(char, int(pos2) - 1, int(pos2))
            if pos1 >= 0 and pos2 >= 0:
                continue
            elif pos1 >= 0:
                valid_passwords_count += 1
            elif pos2 >= 0:
                valid_passwords_count += 1
        print(valid_passwords_count)

    part_one(input)
    part_two(input)
