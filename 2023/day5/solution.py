# What is the lowest location number that corresponds to any of the initial seed numbers?


def get_input_lines_from_file():
    with open("sample", "r") as input_file:
        return input_file.read().splitlines()


def part_one():
    lines = get_input_lines_from_file()
    seeds = [num for num in map(lambda seed: int(seed), lines[0].split(': ')[1].split(" "))]
    maps = {}
    print(seeds)
    line_index = 2
    end_of_map = False
    current_map = ""
    while line_index < len(lines):
        print(line_index, len(lines))
        # if not lines[line_index]:
        #     end_of_map = True
        #     continue
        if lines[line_index].endswith("map:"):
            current_map = lines[line_index].split(" ")[0]
            maps[current_map] = dict.fromkeys(["source", "destination"], dict.fromkeys(["name", "ranges"], list()))
            source, _, destination = current_map.split("-")
            maps[current_map]["source"]["name"] = source
            maps[current_map]["destination"]["name"] = destination
        elif lines[line_index]:
            destination_range_start, source_range_start, range_length = (
                val for val in map(lambda x: int(x), lines[line_index].split(" ")))
            maps[current_map]["source"]["ranges"].append(range(source_range_start, source_range_start + range_length))
            maps[current_map]["destination"]["ranges"].append(
                range(destination_range_start, destination_range_start + range_length))
        line_index += 1
        end_of_map = False
    print(maps)


if __name__ == "__main__":
    print(part_one())
