import re
import math

def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()
    
    
    
def part_one():
    lines = get_input_lines_from_file()
    products = []
    mul_pattern = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\))|do\(\)|don\'t\(\)")
    skip = False
    for line in lines:
        matches = re.finditer(mul_pattern, line)
        for match in matches:
            print(products)
            print(match.group())
            if match.group() == "do()":
                skip = False
            elif match.group() == "don't()":
                skip = True
            else:
                print("??",match.group())
                if not skip:
                    print("groups are", match.groups())
                    products.append(math.prod([int(match.groups()[1]), int(match.groups()[2])]))

    return sum(products)
            

if __name__ == "__main__":
    print(part_one())