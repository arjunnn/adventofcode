import sys
import os
import re
import math


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one(input):
    actual_rows = []
    latest_row = ""
    for row in input:
        if row:
            latest_row += f" {row}"
        else:
            actual_rows.append(latest_row.strip())
            latest_row = ""
    if latest_row:
        actual_rows.append(latest_row.strip())
    valid_passports = 0
    for row in actual_rows:
        row = row
        fields = set([field.split(":")[0] for field in row.split(" ")])
        if len(fields) == 8:
            valid_passports += 1
            continue
        elif len(fields) == 7 and "cid" not in fields:
            valid_passports += 1
            continue

    return valid_passports


def part_two(input):
    actual_rows = []
    latest_row = ""
    hcl_pattern = re.compile("#([0-9a-f]){6}")
    ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def data_is_valid(data):
        try:
            byr = int(data.get("byr"))
            iyr = int(data.get("iyr"))
            eyr = int(data.get("eyr"))
            hgt = data.get("hgt")
            hcl = data.get("hcl")
            ecl = data.get("ecl")
            pid = data.get("pid")
        except ValueError as e:
            return False

        if not (1920 <= byr <= 2002):
            return False
        if not (2010 <= iyr <= 2020):
            return False
        if not (2020 <= eyr <= 2030):
            return False
        try:
            unit = hgt[-2:]
            value = int(hgt[:-2])
            if unit == "cm":
                if not (150 <= value <= 193):
                    return False
            elif unit == "in":
                if not (59 <= value <= 76):
                    return False
            else:
                return False
        except ValueError:
            return False
        if not hcl_pattern.fullmatch(hcl):
            return False
        if ecl not in ecl_values:
            return False
        if len(pid) != 9 or not pid.isdigit():
            return False
        return True

    for row in input:
        if row:
            latest_row += f" {row}"
        else:
            actual_rows.append(latest_row.strip())
            latest_row = ""
    if latest_row:
        actual_rows.append(latest_row.strip())
    valid_passports = 0
    for row in actual_rows:
        row = row
        fields = {field.split(":")[0]: field.split(":")[1] for field in row.split(" ")}
        fieldset = set(fields.keys())
        if len(fieldset) < 7:
            continue
        elif len(fieldset) == 8:
            if data_is_valid(fields):
                valid_passports += 1
                continue
        elif len(fieldset) == 7 and "cid" not in fieldset:
            if data_is_valid(fields):
                valid_passports += 1
                continue

    return valid_passports


print(part_one(get_input_lines_from_file()))
print(part_two(get_input_lines_from_file()))
